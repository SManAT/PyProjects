import threading
import subprocess


class LoadFoto(threading.Thread):
  """
  Schnittstelle zum Raspberry Pi
  Lade ein Foto von der Kamera
  """

  fotoname = "/home/schule/img.jpg"

  def __init__(self):
    pass

  def run(self, *args, **kwargs):
    """ call the Camera """
    cmd = f"raspistill -o {self.fotoname}"

    proc = subprocess.Popen(cmd, shell=True)
    # wait for Process to finish
    exit_code = proc.wait()
    return exit_code
