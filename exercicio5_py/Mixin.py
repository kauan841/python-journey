class LogMixix:
    def log(self,msg):
        print(msg)


class Usuario(LogMixix):
    pass



usuario = Usuario()
usuario.log("maria tem 16 anos")


