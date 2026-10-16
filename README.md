# Dishwasher Math

Dishwasher honesty. The half-empty load felt frugal, and the gallons were always going to add up. Dishwasher Math turns household dishes, half-empty runs and pod spending into honest arithmetic on labeled norms.

## What it computes

- **The load truth** - six pieces per person per day against the washer's capacity: how many days a full rack honestly takes.
- **The half-load truth** - half-empty loads a week at gallons per load, added to extra gallons a year.
- **The pod truth** - loads a week as pods and dollars a year, rounded to the cent.

## Boundary

Dishwasher Math keeps labeled-norm arithmetic only. The six pieces per person-day, the four gallons per load and the pod costs are labeled norms, not measurements of your washer, your water or your household. Check your washer's manual, follow your detergent's dosing over anything this page says, and scrape, don't rinse.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (23 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/dishwashermath/
Repo: https://github.com/iLanis-agent/dishwashermath
