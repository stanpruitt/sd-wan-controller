import time
import spec
import util

if __name__ == "__main__":
    thespec = spec.Spec()
    theutil = util.Util()

    theutil.http_post("/tunnel/create", thespec.spec())

    time.sleep(1)