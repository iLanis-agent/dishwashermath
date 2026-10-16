// Dishwasher Math engine - hypothetical arithmetic on labeled norms only.
// Pieces per person-day, gallons per load and pod costs are labeled norms,
// not measurements of your washer, your water or your household.

function plural(n, one, many) { return n === 1 ? one : many; }
function tenths(x) { return Math.floor(x * 10 + 0.5) / 10; }
function cents(x) { return Math.floor(x * 100 + 0.5) / 100; }
function fixed1(x) { return tenths(x).toFixed(1); }
function money(x) { return cents(x).toFixed(2); }

function loadTruth(people, capacity) {
  if (!(people > 0)) throw new Error("the people must be above zero");
  if (!(capacity > 0)) throw new Error("the capacity must be above zero");
  const pieces = people * 6; // labeled norm: six pieces per person per day
  const days = capacity / pieces;
  return `${people} ${plural(people, "person", "people")} ${people === 1 ? "makes" : "make"} ${pieces} pieces a day; a ${capacity}-piece washer fills in ${fixed1(days)} ${plural(tenths(days), "day", "days")} honestly.`;
}

function halfTruth(halfLoads, gallons) {
  if (!(halfLoads >= 0)) throw new Error("the half-loads must be zero or more");
  if (!(gallons > 0)) throw new Error("the gallons per load must be above zero");
  if (halfLoads === 0) return "0 half-loads a week wastes nothing honestly.";
  const waste = halfLoads * gallons * 52;
  return `${halfLoads} half-${plural(halfLoads, "load", "loads")} a week at ${gallons} gallons each ${halfLoads === 1 ? "runs" : "run"} ${fixed1(waste)} extra gallons a year honestly.`;
}

function podTruth(loads, cost) {
  if (!(loads > 0)) throw new Error("the loads must be above zero");
  if (!(cost > 0)) throw new Error("the pod cost must be above zero");
  const pods = loads * 52;
  return `${loads} ${plural(loads, "load", "loads")} a week ${loads === 1 ? "is" : "is"} ${fixed1(pods)} pods a year - at $${money(cost)} each, $${money(pods * cost)} honestly.`;
}

if (typeof module !== "undefined") {
  module.exports = { loadTruth, halfTruth, podTruth };
}
