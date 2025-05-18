import os
import subprocess
import logging
import sys

class Command:
    def __init__(self):
        self.set_logger()


    def set_logger(self):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(name)s -%(levelname)s - %(message)s",
            handlers=[
                logging.StreamHandler(),
                logging.FileHandler("Command.log")
            ]
        )
        self.logger = logging.getLogger(self.__class__.__name__)

    def run_command(self, command, timeout=None, shell=False, cwd=None):
        try:
            result = subprocess.run(
                command,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                universal_newlines=True,
                timeout=timeout,
                cwd=cwd
            )
            
            output = result.stdout.strip()
            return (True, output)

        except subprocess.TimeoutExpired:
            return (False, output)
        
        except Exception as e:
            return (False, str(e))
        

    def exec(self):
        result, output = self.run_command(['ls', '-l'], timeout=5, shell=True)
        if result:
            self.logger.info(f"Command executud successfully")
        else:
            self.logger.error(f"Command failed with error: {output}")
    
    
    def main(self):
        self.exec()

if __name__ == "__main__":
    Command().main()
        


            

