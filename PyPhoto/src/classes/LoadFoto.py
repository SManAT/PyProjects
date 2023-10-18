import threading
import subprocess


class LoadFoto(threading.Thread):
  """
  Schnittstelle zum Raspberry Pi
  Lade ein Foto von der Kamera
  """

  fotoname = "/home/schule/img.jpg"

  def __init__(self):
    # calls Constructor from Parent
    super().__init__()
    self._stderr = ""
    self._stdout = ""

  def getStderr(self):
    return self._stderr

  def getStdout(self):
    return self._stdout

  def run(self, *args, **kwargs):
    """ call the Camera """
    self._stderr = ""
    self._stdout = ""
    print("Loading Foto ...")

    cmd = f"raspistill -o {self.fotoname}"
    proc = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    for line in iter(proc.stderr.readline, b''):
        self._stderr += line.decode('utf-8', 'ignore')

    for line in iter(proc.stdout.readline, b''):
        self._stdout += line.decode('utf-8', 'ignore')
    proc.communicate()

    # wait for Process to finish
    exit_code = proc.wait()
    return exit_code
