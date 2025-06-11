![image](https://github.com/user-attachments/assets/847be590-097f-4f9e-a6cd-67b873514b1d)# The Evolution - Predator-Prey Neural Network Simulation 🧬

An evolutionary simulation where predators and prey species evolve their behavior through neural networks and genetic algorithms. Watch as artificial intelligence emerges through natural selection in real-time!

## 🎯 Overview

This project simulates an ecosystem where:
- **Green circles (Prey)** try to survive and reproduce
- **Red circles (Predators)** hunt prey to survive and reproduce
- Both species use neural networks to make movement decisions
- Evolution occurs through genetic algorithms with mutation
- Successful behaviors are passed to the next generation

## 🎥 Demo

[![Simulation Demo](image.png)](running.mp4)

*Watch the evolution in action - prey learning to evade, predators learning to hunt*

## 🧠 How It Works

### Neural Network Architecture
- **Input Layer**: 36 neurons (360° vision divided into 10° segments)
- **Hidden Layer**: 200 neurons with sigmoid activation
- **Output Layer**: 9 neurons (8 directions + stay still)
- **Vision Range**: 300 pixels radius

### Evolutionary Algorithm
1. **Selection**: Fitness-based selection of parents
2. **Reproduction**: Top performers create offspring
3. **Mutation**: Random weight modifications for genetic diversity
4. **Survival**: Natural selection through predator-prey interactions

### Fitness Calculation
- **Prey Fitness**: Survival time (longer survival = higher fitness)
- **Predator Fitness**: Number of prey caught + survival time
- **Generation Cycle**: 10 iterations before major evolution step

## 🚀 Features

- **Real-time Evolution**: Watch behaviors change over generations
- **Neural Network Visualization**: 360° vision system for each agent
- **Genetic Algorithm**: Mutation and selection pressure
- **Population Dynamics**: Birth, death, and reproduction cycles
- **Collision Detection**: Sophisticated interaction system
- **Wraparound World**: Toroidal world boundaries

## 📋 Requirements

```txt
pygame
numpy
sys
random
```

## 🛠️ Installation

1. Clone the repository:
```bash
git clone "https://github.com/AkhshanAchu/Sim-Evol.git"
cd Sim-Evol
```

2. Install dependencies:
```bash
pip install pygame numpy
```

3. Run the simulation:
```bash
python evolution_simulation.py
```

## 🎮 Controls

- **Close Window**: Click the X button to exit
- **Automatic Evolution**: The simulation runs autonomously
- **Console Output**: Monitor fitness scores and generation progress

## 🧬 Simulation Parameters

| Parameter | Value | Description |
|-----------|-------|-------------|
| World Size | 800x600 | Simulation area |
| Vision Range | 300px | Agent detection radius |
| Population | 5 prey, 5 predators | Starting population |
| Speed | 8 pixels/frame | Movement speed |
| FPS | 30 | Simulation speed |
| Mutation Rate | Variable | Dynamic mutation based on performance |

## 📊 Evolution Mechanics

### Prey Behavior Evolution
- **Early Generations**: Random movement
- **Mid Generations**: Basic predator avoidance
- **Late Generations**: Sophisticated evasion strategies

### Predator Behavior Evolution
- **Early Generations**: Random hunting
- **Mid Generations**: Basic prey tracking
- **Late Generations**: Advanced hunting strategies

### Key Evolution Events
- **Reproduction Trigger**: Prey reproduce every 8 seconds (240 frames)
- **Predator Success**: Predators reproduce immediately after successful hunt
- **Generation Timeout**: Predators die after 8 seconds without success
- **Major Evolution**: Every 10 generations, top performers become new base population

## 🔬 Technical Details

### Neural Network Structure
```python
class nn:
    def __init__(self, input_nodes=36, output_nodes=9):
        self.layer1_size = 200
        self.weights1 = random_weights(layer1_size, input_nodes+1)
        self.weights2 = random_weights(output_nodes, layer1_size+1)
```

### Vision System
- **360° Awareness**: 36 directional sensors (10° each)
- **Distance Detection**: Closer objects have stronger signals
- **Species Recognition**: Different neural pathways for prey/predator detection

### Movement System
- **8-Directional Movement**: Cardinal + diagonal directions
- **Physics**: Diagonal movement uses √2 speed compensation
- **Boundary Handling**: Toroidal wraparound at screen edges

## 📈 Performance Metrics

The simulation tracks:
- Average fitness per generation
- Best individual fitness scores
- Population survival rates
- Evolution convergence patterns

## 🎨 Visualization

- **Green Circles**: Prey agents
- **Red Circles**: Predator agents
- **Real-time Movement**: Smooth 30 FPS animation
- **Population Display**: Live agent counts

## 🧪 Experiments to Try

1. **Modify Vision Range**: Change the `vision` parameter
2. **Adjust Population Size**: Vary starting populations
3. **Mutation Rate**: Experiment with different mutation strategies
4. **Speed Variations**: Give predators/prey different speeds
5. **World Size**: Try different environment sizes

## 📚 Learning Outcomes

This simulation demonstrates:
- **Emergent Behavior**: Complex strategies from simple rules
- **Neural Network Applications**: AI decision-making systems
- **Genetic Algorithms**: Evolution-based optimization
- **Population Dynamics**: Ecological modeling
- **Artificial Life**: Self-organizing systems


**Watch evolution unfold before your eyes! 🌱➡️🧬➡️🚀**

*"Nothing in biology makes sense except in the light of evolution."* - Theodosius Dobzhansky
