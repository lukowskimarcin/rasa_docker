from rasa.nlu.model import Interpreter
import tarfile
import shutil


def run_nlu(model_path, text):
    tar = tarfile.open(model_path, "r:gz")
    tar.extractall(path="./models/unpack")
    tar.close()

    interpreter = Interpreter.load("./models/unpack/nlu")
    response = interpreter.parse(text)

    shutil.rmtree("./models/unpack")
    return response


if __name__ == '__main__':
    print(run_nlu("./models/20200814-153208.tar.gz", "hi"))
