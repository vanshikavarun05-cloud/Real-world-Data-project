# Sample Superstore – Real-World Data Analysis

## Files
- `real_world_project.py`: executable Python analysis script
- `real_world_project.ipynb`: valid Jupyter Notebook version of the same workflow
- `SampleSuperstore.csv`: dataset (place this file in the project folder)
- `requirements.txt`: required Python packages
- `outputs/`: generated charts (created when the script/notebook runs)

## Run locally
```bash
python -m pip install -r requirements.txt
python real_world_project.py
```

## Run in Jupyter
Open `real_world_project.ipynb`, ensure `SampleSuperstore.csv` is in the same folder, and run all cells.

## Important chart interpretation
The category and region bar charts use grouped sums, so they show **total sales** and **total profit**. The correlation heatmap uses Sales, Quantity, Discount and Profit; identifier fields such as Row ID and Postal Code are excluded.
