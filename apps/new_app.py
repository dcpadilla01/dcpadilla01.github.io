# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo==0.13.15",
#     "polars==1.19.0",
#     "altair==5.5.0",
#     "numpy==2.2.1",
#     "pyarrow==22.0.0",
#     "pandas==2.3.3",
# ]
# ///

import marimo

__generated_with = "0.13.15"
app = marimo.App(width="full")


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import altair as alt
    import numpy as np
    import pyarrow as pa
    return alt, mo, pl


@app.cell
def _(mo, pl):
    # Load the data
    file_location = mo.notebook_location() / "public/denue_inegi_06_.csv"
    raw_df = pl.read_csv(
        str(file_location),
        encoding="latin1",
        null_values=["SN", "sn", "S/N", "s/n", "N/A", "n/a", ""],
        infer_schema_length=10000
    )
    return (raw_df,)


@app.cell
def _():
    # Display basic dataset information
    return


@app.cell
def _(pl, raw_df):
    # Show column names and types
    schema_info = pl.DataFrame({
        "Column": raw_df.columns,
        "Type": [str(dtype) for dtype in raw_df.dtypes]
    })

    return


@app.cell
def _(mo, raw_df):
    # Select relevant columns for analysis
    # Common DENUE columns include: nombre_act (business name), codigo_act (activity code),
    # nom_estab (establishment name), raz_social (business name), etc.

    column_selector = mo.ui.multiselect(
        options=raw_df.columns,
        value=raw_df.columns[:5],  # Default to first 5 columns
        label="Select columns to display in preview"
    )
    column_selector
    return (column_selector,)


@app.cell
def _(column_selector, mo, raw_df):
    # Show data preview with selected columns
    if column_selector.value:
        preview_df = raw_df.select(column_selector.value).head(100)
        _preview_output = mo.ui.table(preview_df, label="Data Preview (first 100 rows)")
    else:
        _preview_output = mo.md("*Select at least one column to preview data*")
    return


@app.cell
def _():
    return


@app.cell
def _(raw_df):
    # Identify activity-related columns (common in DENUE: codigo_act, nombre_act, etc.)
    activity_columns = [col for col in raw_df.columns if 'act' in col.lower() or 'actividad' in col.lower()]
    activity_columns
    return (activity_columns,)


@app.cell
def _(activity_columns):
    activity_columns
    return


@app.cell
def _(activity_columns, mo):
    # Let user select which activity column to analyze
    if activity_columns:
        print("Fi")
        activity_selector = mo.ui.dropdown(
            options=activity_columns,
            value=activity_columns[0] if activity_columns else None,
            label="Select activity column to analyze"
        )
        _activity_output = activity_selector
    else:
        _activity_output = mo.md("*No activity-related columns found*")
        activity_selector = None
    return (activity_selector,)


@app.cell
def _(activity_selector):
    activity_selector
    return


@app.cell
def _(activity_selector, alt, mo, pl, raw_df):
    # Top business activities
    if activity_selector is not None and activity_selector.value:
        activity_col = activity_selector.value

        top_activities = (
            raw_df
            .group_by(activity_col)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
            .head(20)
        )

        chart = alt.Chart(top_activities.to_pandas()).mark_bar().encode(
            x=alt.X("count:Q", title="Number of Businesses"),
            y=alt.Y(f"{activity_col}:N", sort="-x", title="Activity"),
            tooltip=[activity_col, "count"]
        ).properties(
            title=f"Top 20 Business Activities",
            width=600,
            height=400
        )

        _activity_chart = mo.ui.altair_chart(chart)
    else:
        _activity_chart = mo.md("*Select an activity column to see the analysis*")
    return (chart,)


@app.cell
def _(chart, mo):
    mo.ui.altair_chart(chart)
    return


@app.cell
def _(raw_df):
    # Identify location-related columns
    location_columns = [
        col for col in raw_df.columns
        if any(keyword in col.lower() for keyword in ['municipio', 'localidad', 'entidad', 'calle', 'colonia'])
    ]
    location_columns
    return (location_columns,)


@app.cell
def _(location_columns, mo):
    # Let user select location column for geographic analysis
    if location_columns:
        location_selector = mo.ui.dropdown(
            options=location_columns,
            value=location_columns[0] if location_columns else None,
            label="Select geographic column to analyze"
        )
        _location_output = location_selector
    else:
        _location_output = mo.md("*No location-related columns found*")
        location_selector = None
    return (location_selector,)


@app.cell
def _(location_selector):
    location_selector
    return


@app.cell
def _(alt, location_selector, mo, pl, raw_df):
    # Geographic distribution analysis
    if location_selector is not None and location_selector.value:
        location_col = location_selector.value

        geo_distribution = (
            raw_df
            .group_by(location_col)
            .agg(pl.len().alias("count"))
            .sort("count", descending=True)
            .head(15)
        )

        geo_chart = alt.Chart(geo_distribution.to_pandas()).mark_bar().encode(
            x=alt.X("count:Q", title="Number of Businesses"),
            y=alt.Y(f"{location_col}:N", sort="-x", title=location_col.replace("_", " ").title()),
            color=alt.Color("count:Q", scale=alt.Scale(scheme="blues")),
            tooltip=[location_col, "count"]
        ).properties(
            title=f"Business Distribution by {location_col.replace('_', ' ').title()}",
            width=600,
            height=400
        )

        _geo_chart = mo.ui.altair_chart(geo_chart)
    else:
        _geo_chart = mo.md("*Select a location column to see geographic distribution*")
    return (geo_chart,)


@app.cell
def _(geo_chart, mo):
    mo.ui.altair_chart(geo_chart)
    return


@app.cell
def _(raw_df):
    # Look for employment/size columns (per_ocu, estrato, num_local, etc.)
    size_columns = [
        col for col in raw_df.columns
        if any(keyword in col.lower() for keyword in ['per_ocu', 'personal', 'estrato', 'empleado'])
    ]
    size_columns
    return (size_columns,)


@app.cell
def _(mo, pl, raw_df, size_columns):
    # Employment size distribution
    if size_columns:
        size_col = size_columns[0]  # Use first size column found

        # Filter out nulls and get distribution
        size_distribution = (
            raw_df
            .filter(pl.col(size_col).is_not_null())
            .group_by(size_col)
            .agg(pl.len().alias("count"))
            .sort(size_col)
        )

        _size_output = mo.ui.table(size_distribution, label=f"Distribution by {size_col.replace('_', ' ').title()}")
    else:
        _size_output = mo.md("*No employment/size columns found*")
    return size_col, size_distribution


@app.cell
def _(mo, size_col, size_distribution):
    mo.ui.table(size_distribution, label=f"Distribution by {size_col.replace('_', ' ').title()}")
    return


@app.cell
def _(pl, raw_df):
    # Calculate null percentages for each column
    null_stats = pl.DataFrame({
        "Column": raw_df.columns,
        "Null Count": [raw_df[col].null_count() for col in raw_df.columns],
        "Null %": [round(raw_df[col].null_count() / raw_df.height * 100, 2) for col in raw_df.columns]
    }).sort("Null %", descending=True)

    return


@app.cell
def _():
    return


@app.cell
def _():
    return


@app.cell
def _():
    return


if __name__ == "__main__":
    app.run()
