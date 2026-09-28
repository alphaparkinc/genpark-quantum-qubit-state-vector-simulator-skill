from client import QubitStateVectorSimulator

def run_example():
    print("=== GenPark Qubit State Vector Simulator Example ===")
    sim = QubitStateVectorSimulator(2)
    print("State Vector:", sim.benchmark_state_vector())

if __name__ == "__main__":
    run_example()
