from libs.decorator import lockfile_manager


class ShExecute():

    def __init__(self, lock_file):
        pass

    # TODO: デコレータにどうやって引数を渡すか
    @lockfile_manager(lock_file)
    def execute(self):
        pass

s = ShExecute('/tmp/test.lock')
s.execute()
