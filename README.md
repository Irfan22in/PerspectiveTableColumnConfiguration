# PerspectiveTableColumnConfiguration

A Jython shared library for dynamically creating and configuring Ignition Perspective table component column properties.

## Overview

This library provides a set of classes to dynamically build and configure table columns in Ignition Perspective. It allows you to create column configurations programmatically based on your data schema and apply them to table components.

## Features

- **PerspectiveColumnProps**: Base class with all Ignition Perspective table column attributes
- **SchemaColumnInformation**: Column class with database metadata and UI display name support
- **TableComponentColumnConfiguration**: Builds column configurations from table component data
- **ViewRobotDetails**: Example view-specific configuration class
- **ColumnConfigurator**: Fluent API for easy column configuration

## Installation

Copy the `shared_library/perspective_column_config.py` file to your Ignition shared library folder.

## Usage

### Basic Usage in Ignition Change Script

In your table component's `props.data` change script:

```python
# Import from shared library
from shared.perspective_column_config import ViewRobotDetails

# Change script for table.props.data
if len(currentValue.value) > 0:
    table_component = self
    ViewRobotDetails(table_component)
```

### Creating Column Configurations

```python
from shared_library.perspective_column_config import PerspectiveColumnProps

# Create a column configuration
col = PerspectiveColumnProps(field="Robot__name")

# Configure using method chaining
(col
    .set_visible(True)
    .set_editable(False)
    .set_render("string")
    .set_sortable(True)
    .set_filter_enabled(True)
    .set_header_title("Robot Name")
    .set_null_format_value("N/A"))

# Convert to dictionary for Ignition
config = col.to_dict()
```

### Using SchemaColumnInformation with Data Types

```python
from shared_library.perspective_column_config import SchemaColumnInformation

# Columns with automatic render type based on data type
columns = [
    SchemaColumnInformation("Robot__id", ui_display_name="ID", data_type="integer"),
    SchemaColumnInformation("Robot__name", ui_display_name="Robot Name", data_type="varchar"),
    SchemaColumnInformation("Robot__temperature", ui_display_name="Temperature", data_type="float"),
    SchemaColumnInformation("Robot__isActive", ui_display_name="Active", data_type="boolean"),
    SchemaColumnInformation("Robot__createdAt", ui_display_name="Created", data_type="datetime"),
]
```

### Using TableComponentColumnConfiguration

```python
from shared_library.perspective_column_config import TableComponentColumnConfiguration

# Simulate table data
table_data = [
    {"Robot__id": 1, "Robot__name": "Alpha-001", "Robot__status": "active"},
    {"Robot__id": 2, "Robot__name": "Beta-002", "Robot__status": "idle"}
]

# Create configuration from data
config = TableComponentColumnConfiguration(table_data)

# Configure columns with method chaining
(config
    .set_column_visible("Robot__id", False)
    .set_column_header_title("Robot__name", "Robot Name")
    .set_column_editable("Robot__name", True)
    .set_column_header_title("Robot__status", "Status")
    .set_column_render("Robot__status", "string"))

# Build columns for Ignition
columns = config.build_columns()
```

### Using the Fluent API with ColumnConfigurator

```python
from shared_library.perspective_column_config import ViewRobotDetails

# Create view-specific configuration
view = ViewRobotDetails(table_data)

# Use fluent API for configuration
(view.configure_column("Robot__id")
    .visible(False)
    .header_title("ID")
    .done())

(view.configure_column("Robot__name")
    .visible(True)
    .editable(True)
    .render("string")
    .sortable(True)
    .filter_enabled(True)
    .header_title("Robot Name")
    .null_format_value("N/A")
    .done())

(view.configure_column("Robot__status")
    .visible(True)
    .render("view")
    .view_path("/Embedded/StatusIndicator")
    .view_params({"status": "{value}"})
    .header_title("Status")
    .done())

# Build columns
columns = view.build_columns()
```

### Creating Custom View Classes

```python
from shared_library.perspective_column_config import TableComponentColumnConfiguration

class ViewInventoryList(TableComponentColumnConfiguration):
    def __init__(self, table_component):
        super(ViewInventoryList, self).__init__(table_component)
        self._configure_inventory_columns()
        self.apply_to_table()
    
    def _configure_inventory_columns(self):
        self.set_column_visible("Inventory__id", False)
        
        (self.configure_column("Inventory__itemName")
            .header_title("Item Name")
            .sortable(True)
            .filter_enabled(True)
            .done())
        
        (self.configure_column("Inventory__quantity")
            .header_title("Qty")
            .number_format("0,0")
            .render("number")
            .done())
```

## Column Properties

### Available Render Options
- `"auto"`, `"number"`, `"date"`, `"boolean"`, `"string"`, `"view"`

### Available Justify Options
- `"auto"`, `"left"`, `"center"`, `"right"`

### Available Align Options
- `"top"`, `"center"`, `"bottom"`

### Available Sort Options
- `"none"`, `"ascending"`, `"descending"`

### Available Boolean Display Options
- `"value"`, `"checkbox"`, `"toggle"`

### Available Number Display Options
- `"value"`, `"progress"`

### Available Null Format Options
- `"blank"`, `"N/A"`, `null`

### Available Date Format Options
- `"MM/DD/YYYY"`, `"MM/DD/YYYY HH:mm:ss"`

## Column Methods

The following methods are available for configuring individual columns:

| Method | Description |
|--------|-------------|
| `set_visible(value)` | Set column visibility |
| `set_editable(value)` | Set column editability |
| `set_render(value)` | Set render type |
| `set_sortable(value)` | Set if column is sortable |
| `set_filter_enabled(value)` | Enable/disable filtering |
| `set_view_path(value)` | Set path for embedded view |
| `set_view_params(value)` | Set parameters for embedded view |
| `set_null_format_value(value)` | Set null format value |
| `set_header_title(value)` | Set header title |
| `set_number_format(value)` | Set number format |
| `set_date_format(value)` | Set date format |

## Schema Column Naming Convention

Column names should follow the format: `Table__columnName`

For example:
- `Robot__id`
- `Robot__name`
- `Robot__status`
- `Inventory__itemName`

## Running Tests

```bash
cd /path/to/PerspectiveTableColumnConfiguration
python -m unittest discover -s tests -v
```

## Running Examples

```bash
cd /path/to/PerspectiveTableColumnConfiguration
python examples/example_usage.py
```

## Project Structure

```
PerspectiveTableColumnConfiguration/
├── README.md
├── shared_library/
│   ├── __init__.py
│   └── perspective_column_config.py
├── tests/
│   ├── __init__.py
│   └── test_perspective_column_config.py
└── examples/
    └── example_usage.py
```

## Column Properties Reference

```python
# Full column properties structure
{
  "field": "table_columnName",
  "visible": True,
  "editable": False,
  "render": "auto",         # "auto", "number", "date", "boolean", "string", "view"
  "justify": "auto",        # "auto", "left", "center", "right"
  "align": "center",        # "top", "center", "bottom"
  "resizable": True,
  "sortable": True,
  "sort": "none",           # "none", "ascending", "descending"
  "filter": {
    "enabled": False,
    "visible": "on-hover",
    "string": {"condition": "", "value": ""},
    "number": {"condition": "", "value": ""},
    "boolean": {"condition": ""},
    "date": {"condition": "", "value": ""}
  },
  "viewPath": "",
  "viewParams": {},
  "boolean": "checkbox",    # "value", "checkbox", "toggle"
  "number": "value",        # "value", "progress"
  "progressBar": {
    "max": 100,
    "min": 0,
    "bar": {"color": "", "style": {"classes": ""}},
    "track": {"color": "", "style": {"classes": ""}},
    "value": {"enabled": True, "format": "0,0.##", "justify": "center", "style": {"classes": ""}}
  },
  "toggleSwitch": {
    "color": {"selected": "", "unselected": ""}
  },
  "nullFormat": {
    "includeNullStrings": False,
    "strict": False,
    "nullFormatValue": ""   # "blank", "N/A", null
  },
  "numberFormat": "0,0.##",
  "dateFormat": "MM/DD/YYYY",  # "MM/DD/YYYY", "MM/DD/YYYY HH:mm:ss"
  "width": 200,
  "strictWidth": False,
  "style": {"classes": ""},
  "header": {
    "title": "UI Display name",
    "justify": "left",      # "left", "center", "right"
    "align": "center",      # "top", "center", "bottom"
    "style": {"classes": ""}
  },
  "footer": {
    "title": "",
    "justify": "left",
    "align": "center",
    "style": {"classes": ""}
  }
}
```

## License

This project is provided as-is for use with Ignition by Inductive Automation.
