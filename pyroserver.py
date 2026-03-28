import math
import Pyro4

@Pyro4.expose
class MathOperations:
    def add(self, a, b):
        return float(a) + float(b)

    def sub(self, a, b):
        return float(a) - float(b)

    def mul(self, a, b):
        return float(a) * float(b)

    def div(self, a, b):
        a = float(a)
        b = float(b)
        if b == 0:
            raise ValueError("Division by zero is not allowed")
        return a / b

    def mod(self, a, b):
        a = float(a)
        b = float(b)
        if b == 0:
            raise ValueError("Modulus by zero is not allowed")
        return a % b

    def sqrt(self, a):
        a = float(a)
        if a < 0:
            raise ValueError("Square root of a negative number is not allowed")
        return math.sqrt(a)


def main():
    print(f"[Pyro Server] Setting up server ...")
    daemon = Pyro4.Daemon()
    ns = Pyro4.locateNS()
    math_service = MathOperations()
    uri = daemon.register(math_service)
    ns.register("example.math", uri)

    print("[Pyro Server] Registered 'example.math'")
    print(f"[Pyro Server] URI: {uri}")
    print("[Pyro Server] Ready.")

    daemon.requestLoop()


if __name__ == "__main__":
    main()