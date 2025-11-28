# Perspective Table Column Configuration

A Python module for dynamically building column configurations for Ignition Perspective Table components. This library provides a fluent, type-safe API for creating column definitions programmatically, making it easy to generate table configurations for each Perspective view dynamically.

## Features

- **Fluent API**: Chain methods to build complex column configurations easily
- **Type Detection**: Automatically detect and configure columns based on field names
- **Pre-built Column Types**: Quick methods for common column types (text, number, date, boolean, etc.)
- **Custom Styling**: Apply CSS styles to columns
- **Embedded Views**: Configure columns with embedded Perspective views
- **Reusable Templates**: Create reusable column configuration templates
- **JSON Export**: Export configurations as JSON for use in Perspective

## Installation

Copy the `perspective_table_config` folder to your Ignition project's script library, or use it directly in your Python scripts.

```python
# In Ignition, add to Project Library Scripts
from perspective_table_config import ColumnBuilder, ColumnConfig, TableColumnsBuilder
```

## Quick Start

### Basic Usage

```python
from perspective_table_config import ColumnBuilder, ColumnConfig

# Build columns using factory methods
columns = [
    ColumnBuilder.id_column("user_id", "ID", 60).build(),
    ColumnBuilder.text("username", "Username", width=150).build(),
    ColumnBuilder.boolean("is_active", "Active", "Yes", "No", width=80).build(),
    ColumnBuilder.date("created_date", "Registered", "YYYY-MM-DD", width=120).build(),
]

# Apply to table component
self.props.columns = columns
```

### Fluent API

```python
from perspective_table_config import ColumnConfig

# Build complex columns with method chaining
column = (ColumnConfig("order_id")
    .header(title="Order #", tooltip="Unique order identifier")
    .width(value=100, min_width=80, max_width=150)
    .justify("center")
    .sortable(True)
    .editable(False)
    .style(font_weight="bold", color="#2e7d32")
    .build())
```

### Automatic Column Generation

```python
from perspective_table_config import TableColumnsBuilder

# Generate columns from data automatically
data = [
    {"id": 1, "name": "Product A", "price": 29.99, "is_active": True},
    {"id": 2, "name": "Product B", "price": 49.99, "is_active": False}
]

builder = TableColumnsBuilder()
builder.set_default_settings(sortable=True, editable=False)
builder.exclude_fields("internal_id")

columns = builder.from_data(data).build()
```

## Column Types

### Text Column

```python
ColumnBuilder.text("name", "Full Name", width=200)
```

### Number Column

```python
ColumnBuilder.number("quantity", "Qty", decimals=0, width=80)
```

### Currency Column

```python
ColumnBuilder.currency("price", "Price", "$", decimals=2, width=100)
```

### Date Column

```python
ColumnBuilder.date("birth_date", "Birthday", "MM/DD/YYYY", width=120)
```

### DateTime Column

```python
ColumnBuilder.datetime("timestamp", "Timestamp", "YYYY-MM-DD HH:mm:ss", width=150)
```

### Boolean Column

```python
ColumnBuilder.boolean("active", "Status", "Active", "Inactive", width=80)
```

### Toggle Column

```python
ColumnBuilder.toggle("enabled", "Enable", width=60)
```

### Progress Bar Column

```python
ColumnBuilder.progress("completion", "Progress", min_value=0, max_value=100, show_value=True, width=150)
```

### Embedded View Column

```python
ColumnBuilder.view("status", "Views/StatusBadge", "Status", params={"color": "auto"}, width=100)
```

## Using with Perspective Property Change Scripts

```python
def on_data_change(self, event):
    """Property change script for props.data"""
    from perspective_table_config import TableColumnsBuilder
    
    data = self.props.data
    if not data or len(data) == 0:
        return
    
    builder = TableColumnsBuilder()
    builder.set_default_settings(sortable=True, editable=False)
    builder.exclude_fields("_rowNum", "_selected")
    
    columns = builder.from_data(data).build()
    self.props.columns = columns
```

## Using with Script Transforms

```python
def transform_columns(value, self, session, params):
    """Script transform for column binding"""
    from perspective_table_config import TableColumnsBuilder
    
    if not value:
        return []
    
    builder = TableColumnsBuilder()
    return builder.from_data(value).build()
```

## Advanced Usage

### Custom Type Rules

```python
builder = TableColumnsBuilder()

# Add custom detection rules
builder.add_type_rule(
    "sku",
    lambda f, t: ColumnBuilder.text(f, t).style(font_weight="bold")
)
builder.add_type_rule(
    "qty",
    lambda f, t: ColumnBuilder.number(f, t, decimals=0)
)
```

### Field Overrides

```python
builder = TableColumnsBuilder()
builder.add_field_override(
    "status",
    ColumnConfig("status")
        .header(title="Status")
        .embedded_view("Views/StatusIndicator")
        .width(value=100)
)
```

### Reordering Columns

```python
builder = TableColumnsBuilder()
builder.from_field_list(["name", "id", "status"])
builder.reorder("id", "name")  # ID first, then name, then status
```

### Reusable Templates

```python
class ColumnTemplates:
    @staticmethod
    def audit_columns():
        return [
            ColumnBuilder.text("created_by", "Created By", 120).build(),
            ColumnBuilder.datetime("created_date", "Created Date", "YYYY-MM-DD HH:mm", 150).build(),
            ColumnBuilder.text("modified_by", "Modified By", 120).build(),
            ColumnBuilder.datetime("modified_date", "Modified Date", "YYYY-MM-DD HH:mm", 150).build(),
        ]

# Use template
columns = [
    ColumnBuilder.id_column().build(),
    ColumnBuilder.text("name", "Name", 200).build(),
]
columns.extend(ColumnTemplates.audit_columns())
```

## API Reference

### ColumnConfig

| Method | Description |
|--------|-------------|
| `header(title, tooltip, align)` | Configure column header |
| `width(value, min_width, max_width, grow)` | Configure column width |
| `strict_width(width)` | Set fixed width (min=max=width) |
| `justify(value)` | Set text justification (left, center, right) |
| `visible(is_visible)` | Set column visibility |
| `editable(is_editable)` | Set column editability |
| `sortable(is_sortable)` | Set column sortability |
| `resizable(is_resizable)` | Set column resizability |
| `render(type, **options)` | Set render type and options |
| `number_format(...)` | Configure number formatting |
| `date_format(format_string)` | Configure date formatting |
| `boolean_format(true_text, false_text)` | Configure boolean display |
| `progress_bar(min, max, show_value)` | Configure progress bar |
| `embedded_view(path, params)` | Configure embedded view |
| `style(...)` | Configure CSS styles |
| `filter(enabled, filter_type)` | Configure filtering |
| `build()` | Build the configuration dict |

### ColumnBuilder

| Method | Description |
|--------|-------------|
| `text(field, title, width)` | Create text column |
| `number(field, title, decimals, width)` | Create number column |
| `currency(field, title, symbol, decimals, width)` | Create currency column |
| `date(field, title, format, width)` | Create date column |
| `datetime(field, title, format, width)` | Create datetime column |
| `boolean(field, title, true_text, false_text, width)` | Create boolean column |
| `toggle(field, title, width)` | Create toggle column |
| `progress(field, title, min, max, show_value, width)` | Create progress column |
| `view(field, view_path, title, params, width)` | Create embedded view column |
| `id_column(field, title, width)` | Create ID column |
| `actions_column(view_path, field, title, width, params)` | Create actions column |

### TableColumnsBuilder

| Method | Description |
|--------|-------------|
| `add_type_rule(pattern, factory)` | Add custom type detection rule |
| `set_default_settings(...)` | Set default column settings |
| `exclude_fields(*fields)` | Exclude fields from generation |
| `add_field_override(field, config)` | Override specific field config |
| `add_column(config)` | Add a column directly |
| `from_field_list(fields)` | Generate columns from field names |
| `from_data(data)` | Generate columns from data |
| `from_dataset_columns(dataset)` | Generate from Ignition dataset |
| `reorder(*fields)` | Reorder columns |
| `clear()` | Clear all columns |
| `build()` | Build list of configuration dicts |
| `build_json(indent)` | Build as JSON string |

## Requirements

- Python 3.6+ (or Jython 2.7 for Ignition)
- No external dependencies

## Testing

Run the tests using unittest:

```bash
python -m unittest discover -v tests/
```

## Examples

See the `examples/` directory for more usage examples:

- `perspective_usage_examples.py` - Comprehensive examples for Perspective usage

## License

MIT License