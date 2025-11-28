# -*- coding: utf-8 -*-
"""
Example Usage of Perspective Table Column Configuration

This script demonstrates how to use the Perspective Table Column Configuration
module in Ignition Perspective.

Example Usage in Ignition:
--------------------------
In Ignition, you would typically use this in a change script on table.props.data:

```python
# In the change script for table.props.data
if len(table.props.data) > 0:
    table_component = self
    ViewRobotDetails(table_component)
```
"""

import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from shared_library.perspective_column_config import (
    PerspectiveColumnProps,
    SchemaColumnInformation,
    TableComponentColumnConfiguration,
    ViewRobotDetails,
    ColumnConfigurator
)


def example_basic_column_props():
    """Example: Creating a basic column property configuration."""
    print("=" * 60)
    print("Example 1: Basic PerspectiveColumnProps")
    print("=" * 60)
    
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
    
    print("Field:", config["field"])
    print("Visible:", config["visible"])
    print("Render:", config["render"])
    print("Header Title:", config["header"]["title"])
    print()


def example_schema_column():
    """Example: Using SchemaColumnInformation with metadata."""
    print("=" * 60)
    print("Example 2: SchemaColumnInformation with Data Type")
    print("=" * 60)
    
    # Create columns with different data types
    columns = [
        SchemaColumnInformation("Robot__id", ui_display_name="ID", data_type="integer"),
        SchemaColumnInformation("Robot__name", ui_display_name="Robot Name", data_type="varchar"),
        SchemaColumnInformation("Robot__temperature", ui_display_name="Temperature", data_type="float"),
        SchemaColumnInformation("Robot__isActive", ui_display_name="Active", data_type="boolean"),
        SchemaColumnInformation("Robot__createdAt", ui_display_name="Created", data_type="datetime"),
    ]
    
    for col in columns:
        print("Column: {}".format(col.column_name))
        print("  Table: {}".format(col.table_name))
        print("  Display Name: {}".format(col.ui_display_name))
        print("  Data Type: {}".format(col.data_type))
        print("  Render: {}".format(col.render))
        print()


def example_table_configuration():
    """Example: Using TableComponentColumnConfiguration with mock data."""
    print("=" * 60)
    print("Example 3: TableComponentColumnConfiguration")
    print("=" * 60)
    
    # Simulate table data that would come from a database
    table_data = [
        {
            "Robot__id": 1,
            "Robot__name": "Alpha-001",
            "Robot__status": "active",
            "Robot__batteryLevel": 85.5,
            "Robot__lastSeen": "2023-06-15 10:30:00"
        },
        {
            "Robot__id": 2,
            "Robot__name": "Beta-002",
            "Robot__status": "idle",
            "Robot__batteryLevel": 92.3,
            "Robot__lastSeen": "2023-06-15 10:28:00"
        }
    ]
    
    # Create configuration from data
    config = TableComponentColumnConfiguration(table_data)
    
    # Configure columns
    (config
        .set_column_visible("Robot__id", False)
        .set_column_header_title("Robot__name", "Robot Name")
        .set_column_editable("Robot__name", True)
        .set_column_header_title("Robot__status", "Status")
        .set_column_render("Robot__status", "string")
        .set_column_header_title("Robot__batteryLevel", "Battery %")
        .set_column_number_format("Robot__batteryLevel", "0.0%")
        .set_column_header_title("Robot__lastSeen", "Last Seen")
        .set_column_date_format("Robot__lastSeen", "MM/DD/YYYY HH:mm:ss"))
    
    # Build columns for Ignition
    columns = config.build_columns()
    
    print("Generated {} column configurations:".format(len(columns)))
    for col in columns:
        print("  - {}: visible={}, header='{}'".format(col['field'], col['visible'], col['header']['title']))
    print()


def example_view_specific_configuration():
    """Example: Using ViewRobotDetails for view-specific configuration."""
    print("=" * 60)
    print("Example 4: ViewRobotDetails (View-Specific Configuration)")
    print("=" * 60)
    
    # Simulate table data
    table_data = [
        {"Robot__id": 1, "Robot__name": "Alpha", "Robot__status": "active"}
    ]
    
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
    
    print("ViewRobotDetails configured {} columns:".format(len(columns)))
    for col in columns:
        print("  - {}:".format(col['field']))
        print("      visible: {}".format(col['visible']))
        print("      render: {}".format(col['render']))
        if col['viewPath']:
            print("      viewPath: {}".format(col['viewPath']))
    print()


def example_ignition_change_script():
    """Example: How this would be used in an Ignition change script."""
    print("=" * 60)
    print("Example 5: Ignition Change Script Usage")
    print("=" * 60)
    
    print("""
In Ignition Perspective, you would use this in a change script on table.props.data:

```python
# Import from shared library
from shared.perspective_column_config import ViewRobotDetails

# Change script for table.props.data
if len(currentValue.value) > 0:
    # self is the table component
    table_component = self
    
    # Create and apply column configuration
    view = ViewRobotDetails(table_component)
    
    # Optionally configure specific columns
    (view.configure_column("Robot__name")
        .visible(True)
        .editable(True)
        .header_title("Robot Name")
        .sortable(True)
        .filter_enabled(True)
        .done())
    
    # The ViewRobotDetails constructor automatically applies the configuration
    # Or you can manually apply it:
    # view.apply_to_table()
```
""")


def example_custom_view_class():
    """Example: Creating a custom view-specific class."""
    print("=" * 60)
    print("Example 6: Custom View Class")
    print("=" * 60)
    
    print("""
You can create custom view classes by extending ViewRobotDetails or TableComponentColumnConfiguration:

```python
class ViewInventoryList(TableComponentColumnConfiguration):
    def __init__(self, table_component):
        super(ViewInventoryList, self).__init__(table_component)
        
        # Apply view-specific configurations
        self._configure_inventory_columns()
        
        # Automatically apply to table
        self.apply_to_table()
    
    def _configure_inventory_columns(self):
        # Hide ID column
        self.set_column_visible("Inventory__id", False)
        
        # Configure item name
        (self.configure_column("Inventory__itemName")
            .header_title("Item Name")
            .sortable(True)
            .filter_enabled(True)
            .done())
        
        # Configure quantity with number format
        (self.configure_column("Inventory__quantity")
            .header_title("Qty")
            .number_format("0,0")
            .render("number")
            .done())
        
        # Configure price with currency format
        (self.configure_column("Inventory__price")
            .header_title("Price")
            .number_format("$0,0.00")
            .render("number")
            .done())
```
""")


if __name__ == "__main__":
    example_basic_column_props()
    example_schema_column()
    example_table_configuration()
    example_view_specific_configuration()
    example_ignition_change_script()
    example_custom_view_class()
    
    print("=" * 60)
    print("All examples completed successfully!")
    print("=" * 60)
