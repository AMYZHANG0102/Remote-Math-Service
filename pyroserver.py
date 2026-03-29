import math
import Pyro4

@Pyro4.expose # Expose this class to be accessible via Pyro
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
    
    daemon = Pyro4.Daemon(host="pyroserver") # Create a Pyro daemon that listens on the "pyroserver" hostname (which should resolve to this container's IP address)
    ns = Pyro4.locateNS(host="pyronameserver") # Locate the Pyro name server running on "pyronameserver"
    
    math_service = MathOperations()
    
    uri = daemon.register(math_service) # Register the MathOperations object with the Pyro daemon and get its URI
    ns.register("mathserver", uri) # Register the URI with the Pyro name server "mathserver"

    print("[Pyro Server] Registered 'mathserver'")
    print(f"[Pyro Server] URI: {uri}")
    print("[Pyro Server] Ready.")

    daemon.requestLoop() # Start the request loop to wait for incoming remote method calls and process them


if __name__ == "__main__":
    main()