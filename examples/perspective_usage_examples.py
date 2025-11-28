"""
Example: Dynamic Column Configuration for Ignition Perspective Table

This example demonstrates how to use the perspective_table_config module
to dynamically build column configurations for Perspective Table components.

These examples can be used in:
- Property Change Scripts
- Script Transforms
- Message Handlers
- Other Perspective scripting contexts
"""

# Import the module (in Ignition, add to Project Library Scripts)
from perspective_table_config import ColumnBuilder, ColumnConfig, TableColumnsBuilder
from perspective_table_config.table_columns import build_columns_from_data


# =============================================================================
# Example 1: Basic Usage - Building columns manually
# =============================================================================

def example_basic_columns():
    """
    Build a simple set of columns for a user table.
    Returns column configuration list for props.columns.
    """
    columns = [
        # ID column with fixed width
        ColumnBuilder.id_column("user_id", "ID", 60).build(),
        
        # Text columns
        ColumnBuilder.text("username", "Username", width=150).build(),
        ColumnBuilder.text("email", "Email Address", width=200).build(),
        
        # Boolean column showing active status
        ColumnBuilder.boolean("is_active", "Active", "Yes", "No", width=80).build(),
        
        # Date column for registration date
        ColumnBuilder.date("created_date", "Registered", "YYYY-MM-DD", width=120).build(),
    ]
    return columns


# =============================================================================
# Example 2: Fluent API - Chaining column configuration methods
# =============================================================================

def example_fluent_api():
    """
    Use the fluent API to build columns with more detailed configuration.
    """
    columns = [
        # Complex column configuration using method chaining
        (ColumnConfig("order_id")
            .header(title="Order #", tooltip="Unique order identifier")
            .width(value=100, min_width=80, max_width=150)
            .justify(ColumnConfig.JUSTIFY_CENTER)
            .sortable(True)
            .editable(False)
            .style(font_weight="bold")
            .build()),
        
        # Currency column with custom styling
        (ColumnConfig("total_amount")
            .header(title="Total")
            .number_format(format_string="$0,0.00")
            .justify(ColumnConfig.JUSTIFY_RIGHT)
            .width(value=120)
            .style(color="#2e7d32", font_weight="bold")
            .build()),
        
        # Progress bar column
        (ColumnConfig("completion")
            .header(title="Progress")
            .progress_bar(min_value=0, max_value=100, show_value=True)
            .width(value=150)
            .build()),
        
        # Status column with embedded view
        (ColumnConfig("status")
            .header(title="Status")
            .embedded_view(
                path="Shared/Components/StatusBadge",
                params={"color": "auto"}
            )
            .width(value=100)
            .build()),
    ]
    return columns


# =============================================================================
# Example 3: Automatic Column Generation from Data
# =============================================================================

def example_auto_generate_from_data():
    """
    Automatically generate columns based on the data structure.
    Perfect for dynamic tables where columns aren't known ahead of time.
    """
    # Sample data (would come from props.data in real usage)
    sample_data = [
        {
            "id": 1,
            "name": "Product A",
            "price": 29.99,
            "quantity": 100,
            "is_active": True,
            "created_date": "2024-01-15"
        }
    ]
    
    # Quick way - use the convenience function
    columns = build_columns_from_data(
        data=sample_data,
        exclude_fields=["internal_id"],
        sortable=True,
        editable=False
    )
    return columns


# =============================================================================
# Example 4: Advanced - Using TableColumnsBuilder with custom rules
# =============================================================================

def example_advanced_builder():
    """
    Use TableColumnsBuilder for advanced column generation with custom rules.
    """
    # Create builder
    builder = TableColumnsBuilder()
    
    # Set default column behavior
    builder.set_default_settings(
        sortable=True,
        editable=False,
        resizable=True
    )
    
    # Add custom type detection rules
    builder.add_type_rule(
        "sku",
        lambda f, t: ColumnBuilder.text(f, t).style(font_weight="bold")
    )
    builder.add_type_rule(
        "qty",
        lambda f, t: ColumnBuilder.number(f, t, decimals=0)
    )
    
    # Exclude internal fields
    builder.exclude_fields("internal_id", "metadata", "_version")
    
    # Add custom overrides for specific fields
    builder.add_field_override(
        "status",
        (ColumnConfig("status")
            .header(title="Status")
            .embedded_view("Shared/StatusIndicator")
            .width(value=100))
    )
    
    # Generate from field list
    fields = ["id", "sku", "product_name", "qty", "price", "status", "created_date"]
    columns = builder.from_field_list(fields).build()
    
    return columns


# =============================================================================
# Example 5: Perspective Property Change Script
# =============================================================================

def on_data_change(self, event):
    """
    Example property change script for props.data.
    
    This function would be placed in a Property Change Script on the
    Table component, triggered when props.data changes.
    
    In Ignition, 'self' refers to the component and 'event' contains
    the change information.
    """
    # Get the new data
    data = self.props.data
    
    if not data or len(data) == 0:
        return
    
    # Build columns from the data
    builder = TableColumnsBuilder()
    builder.set_default_settings(sortable=True, editable=False)
    
    # Exclude system fields
    builder.exclude_fields("_rowNum", "_selected")
    
    # Generate columns from data
    columns = builder.from_data(data).build()
    
    # Update the table's columns property
    self.props.columns = columns


# =============================================================================
# Example 6: Working with Ignition Datasets
# =============================================================================

def build_columns_from_dataset(dataset):
    """
    Build columns from an Ignition BasicDataset or PyDataSet.
    
    Args:
        dataset: An Ignition dataset object
        
    Returns:
        List of column configurations
    """
    builder = TableColumnsBuilder()
    
    # Use the dataset-specific method
    builder.from_dataset_columns(dataset)
    
    # Customize order - put important columns first
    builder.reorder("id", "name", "status")
    
    return builder.build()


# =============================================================================
# Example 7: Script Transform for Column Binding
# =============================================================================

def transform_columns(value, self, session, params):
    """
    Script transform for a binding that generates columns from data.
    
    This would be used as a Script Transform on a binding from a
    data source to the props.columns property.
    
    Args:
        value: The incoming data
        self: The component reference
        session: The session object
        params: Transform parameters
        
    Returns:
        Column configuration list
    """
    if not value:
        return []
    
    # Create builder with view-specific settings
    builder = TableColumnsBuilder()
    
    # Apply settings from transform params if provided
    if params.get("editable", False):
        builder.set_default_settings(editable=True)
    
    # Build columns from the data
    return builder.from_data(value).build()


# =============================================================================
# Example 8: Reusable Column Templates
# =============================================================================

class ColumnTemplates:
    """
    Reusable column configuration templates for common patterns.
    """
    
    @staticmethod
    def audit_columns():
        """Standard audit columns (created_by, created_date, etc.)"""
        return [
            ColumnBuilder.text("created_by", "Created By", 120).build(),
            ColumnBuilder.datetime("created_date", "Created Date", 
                                   "YYYY-MM-DD HH:mm", 150).build(),
            ColumnBuilder.text("modified_by", "Modified By", 120).build(),
            ColumnBuilder.datetime("modified_date", "Modified Date",
                                   "YYYY-MM-DD HH:mm", 150).build(),
        ]
    
    @staticmethod
    def status_column(field="status", view_path="Shared/StatusBadge"):
        """Standard status column with embedded view"""
        return (ColumnConfig(field)
                .header(title="Status")
                .embedded_view(view_path)
                .width(value=120)
                .sortable(True)
                .build())
    
    @staticmethod
    def actions_column(view_path="Shared/RowActions", width=150):
        """Standard actions column for row operations"""
        return ColumnBuilder.actions_column(
            view_path=view_path,
            width=width
        ).build()


def example_with_templates():
    """
    Use column templates to build a table configuration.
    """
    # Start with main columns
    columns = [
        ColumnBuilder.id_column().build(),
        ColumnBuilder.text("name", "Name", 200).build(),
        ColumnBuilder.currency("price", "Price", "$", 2, 100).build(),
        ColumnTemplates.status_column(),
    ]
    
    # Add audit columns at the end
    columns.extend(ColumnTemplates.audit_columns())
    
    # Add actions column
    columns.append(ColumnTemplates.actions_column())
    
    return columns


# =============================================================================
# Main - Run examples for testing
# =============================================================================

if __name__ == "__main__":
    import json
    
    print("=" * 60)
    print("Example 1: Basic Columns")
    print("=" * 60)
    print(json.dumps(example_basic_columns(), indent=2))
    
    print("\n" + "=" * 60)
    print("Example 2: Fluent API")
    print("=" * 60)
    print(json.dumps(example_fluent_api(), indent=2))
    
    print("\n" + "=" * 60)
    print("Example 3: Auto-generate from Data")
    print("=" * 60)
    print(json.dumps(example_auto_generate_from_data(), indent=2))
    
    print("\n" + "=" * 60)
    print("Example 4: Advanced Builder")
    print("=" * 60)
    print(json.dumps(example_advanced_builder(), indent=2))
    
    print("\n" + "=" * 60)
    print("Example 8: With Templates")
    print("=" * 60)
    print(json.dumps(example_with_templates(), indent=2))
