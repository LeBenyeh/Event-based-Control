# Convoyeur System Simulation

**Description**: A Python-based simulation of a conveyor system, including components like boxes, collectors, conveyors, corners, detection zones, dispensers, selectors, and transformers. This project models the behavior and interactions of these components in an event-based control system.


---

## Prerequisites

- Python 3.8 or higher
- (Optional) Virtual environment (recommended)

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/convoyeur-system.git
cd convoyeur-system
```

### 2. Create a Virtual Environment
```bash
python -m venv .venv
```

- **Activate the virtual environment**:
  - **Windows**:
    ```bash
    .\.venv\Scripts\activate
    ```
  - **Linux/MacOS**:
    ```bash
    source .venv/bin/activate
    ```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```
---


## Execution

### Run the Simulation

```bash
make run
```
Or, if you don't have ```make```
```bash
python3 simulation.py
```

### Generate UML Diagrams
```bash
make generate
```
*(This will generate UML class diagrams for the system using `pyreverse`.)*

---

## Project Structure

```
convoyeur-system/
│
├── .venv/                  # Virtual environment
├── src/                    # Source code
│   ├── Box.py              # Box component
│   ├── Collector.py        # Collector component
│   ├── Conveyor.py         # Conveyor component
│   ├── Corner.py           # Corner component
│   ├── DetectionZone.py    # Detection zone component
│   ├── Dispenser.py        # Dispenser component
│   ├── Selector.py         # Selector component
│   ├── Transformer.py      # Transformer component
│   ├── SelectorState.py    # Selector state logic
│   ├── SectionType.py      # Section type definitions
│   ├── assets.py           # Asset utilities
│   ├── settings.py         # Simulation settings
│   └── simulation.py       # Main simulation script
├── diagrams/               # Generated UML diagrams
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```


