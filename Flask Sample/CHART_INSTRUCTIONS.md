# Adding a Chart to the Flask Sample App

**Goal:** Read the data in `data.csv` with Flask, send it to the browser as JSON, and draw a bar chart with Chart.js.

```
data.csv  →  Flask route reads it  →  returns JSON
                                          ↓
browser  ←  Chart.js draws chart  ←  script.js requests JSON
```

Work through the steps in order. Each step ends with a ✅ **Checkpoint**. Don't move on until it passes.

---

## Before you start

- [ ] Open the `Flask Sample` folder in VS Code.
- [ ] Run `app.py` and open the app in the browser.
  - ⚠️ The app picks a **random free port** each time it runs. Look in the terminal for a line like `Running on http://127.0.0.1:54321` and use that port number throughout.
- [ ] Look at `data.csv`. Which column holds numbers you could chart? (`data2`.) Which column would make good labels? (`data1`.)
- [ ] Delete the `J,J,J` row from `data.csv`. `"J"` is not a number and will cause an error in Step 1.

✅ **Checkpoint:** The form page loads and the table shows the rows from `data.csv`.

---

## Step 1: Flask route that returns the chart data (`app.py`)

You already have a helper function, `read_csv_data()`, that returns every row as a list, e.g. `['Alice', '42', 'Dublin']`. Reuse it. Don't write the CSV-reading code again.

1. [ ] Below the `/submit` route, add a new route: `@app.route('/chart-data')`.
2. [ ] Inside its function, call `read_csv_data()` and store the result.
3. [ ] Create two empty lists: `labels` and `values`.
4. [ ] Loop through the rows:
   - Add `row[0]` (the name) to `labels`.
   - Add `row[1]` (the number) to `values`. **Convert it to an `int` first**, because everything read from a CSV is a string.
5. [ ] Return the lists with `jsonify`, as a dictionary with two keys: `"labels"` and `"values"`.
   - `jsonify` is already imported at the top of the file.

💡 **Hint:** Look at how the `/submit` route uses `jsonify({...})`. Yours will look very similar.

✅ **Checkpoint:** Restart the app, then visit `http://127.0.0.1:<your-port>/chart-data`. You should see something like:

```json
{"labels": ["Alice", "Brian", ...], "values": [42, 17, ...]}
```

❓ **Check your understanding:**
- Why do the numbers in `values` have no quotes around them, but the names in `labels` do?
- What happens if you visit `/chart-data` with a row like `J,J,J` back in the CSV? Why?

---

## Step 2: Add Chart.js and a canvas to the page (`templates/index.html`)

1. [ ] In the `<head>`, under the jQuery `<script>` line, add a `<script>` tag that loads Chart.js from a CDN:
   ```
   https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.js
   ```
2. [ ] Under the table (but **above** the line that loads `script.js`), add:
   - an `<h2>` heading, e.g. "Chart of Data 2"
   - an empty `<canvas>` element with `id="myChart"`

💡 **Hint:** The canvas is just a blank drawing area. Chart.js will draw onto it in Step 3.

✅ **Checkpoint:** Reload the page. Nothing new is visible yet, which is expected. Open the browser **DevTools** (F12) → **Console** tab. There should be **no red errors**.

---

## Step 3: Request the data and draw the chart (`static/script.js`)

Your script already uses jQuery's `$.ajax` to **send** form data with `POST`. Now you'll do the reverse: **get** data with a `GET` request.

1. [ ] At the **top** of the file (outside `$(document).ready`), create a variable to hold the chart: `let myChart = null;`
2. [ ] Write a function called `loadChart()`. Inside it:
   1. [ ] Use `$.ajax` with `type: 'GET'` and `url: '/chart-data'`. (Or use the shortcut `$.getJSON('/chart-data', function (response) { ... })`.)
   2. [ ] In the `success` function, `response.labels` and `response.values` hold your two lists.
   3. [ ] Find the canvas with `document.getElementById('myChart')`.
   4. [ ] Create the chart with `new Chart(canvas, { ... })` and store it in `myChart`. The settings object needs:
      - `type`: `'bar'`
      - `data.labels`: `response.labels`
      - `data.datasets`: a list with **one** object containing:
        - `label`: a name for the data, e.g. `'Data 2'`
        - `data`: `response.values`
3. [ ] Inside `$(document).ready(...)`, call `loadChart();` so the chart draws when the page opens.

💡 **Hint:** Search for "Chart.js bar chart getting started". The first example on the official docs page has exactly this structure.

✅ **Checkpoint:** Reload the page. A bar chart appears with one bar per name. 🎉

❓ **Check your understanding:**
- Which part of the app does each job: reading the file, transporting the data, drawing the chart?
- What's the difference between the `POST` to `/submit` and the `GET` to `/chart-data`?

---

## Step 4: Update the chart when the form is submitted

At the moment, new rows show up in the table but **not** in the chart until you reload the page.

1. [ ] At the start of `loadChart()`, check whether a chart already exists. If `myChart` is not `null`, call `myChart.destroy()`.
   - Without this, Chart.js gives an error: *"Canvas is already in use"*.
2. [ ] In the `/submit` `success` function (after the table is rebuilt), call `loadChart();`.

✅ **Checkpoint:** Submit a new row with a **number** in Data 2. The chart updates straight away without reloading.

⚠️ **Try this:** Submit a row with text (e.g. `abc`) in Data 2. What happens to `/chart-data`? See Extension 1.

---

## Troubleshooting

| Problem | Likely cause |
|---|---|
| `/chart-data` shows **404 Not Found** | Typo in the route, or the app wasn't restarted after editing `app.py`. |
| `/chart-data` shows **500 Internal Server Error** | A value in column 2 isn't a number. Check the terminal for `ValueError`. |
| Console: `Chart is not defined` | The Chart.js `<script>` tag is missing, misspelt, or placed **after** `script.js`. |
| Console: `Canvas is already in use` | You didn't `destroy()` the old chart before drawing a new one (Step 4). |
| Chart appears but is empty | Check the spelling of `response.labels` / `response.values`. They must match the keys in your `jsonify`. |
| Bars are in the wrong place | `labels` and `values` are different lengths. Check your loop. |

**Debugging tip:** Put `console.log(response);` as the first line of your `success` function, then look in the Console to see exactly what Flask sent.

---

## Extensions

1. **Bad data protection:** In the Flask loop, use `try` / `except ValueError` to **skip** rows where `row[1]` isn't a number, instead of crashing.
2. **Change the chart type:** Try `'line'`, `'pie'` and `'doughnut'`. Which suits this data best, and why?
3. **Sort the data:** Show the bars from highest to lowest. (Hint: sort in Python before returning the JSON.)
4. **Stats:** Return the **average** and **maximum** of `values` in the JSON too, and display them in a `<p>` under the chart.
5. **Count by category:** Make a second chart showing **how many rows each town (`data3`) has**. (Hint: use a dictionary to count in Python.)
6. **Validation:** Change the Data 2 `<input>` to `type="number"` so users can only submit numbers.
