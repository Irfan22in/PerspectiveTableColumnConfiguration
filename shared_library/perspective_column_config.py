# -*- coding: utf-8 -*-
"""
Perspective Table Column Configuration Module

This module provides classes for dynamically creating and configuring
Ignition Perspective table component column properties.

Classes:
    PerspectiveColumnProps: Base class with all Ignition perspective table column attributes
    SchemaColumnInformation: Column with metadata and UI display name
    TableComponentColumnConfiguration: Builds column configurations from table component data
    ViewRobotDetails: Example subclass for RobotDetails view configuration
"""

# Python to Perspective boolean representation
true = True
false = False


class PerspectiveColumnProps(object):
    """
    Base class containing all attributes of an Ignition Perspective table column.
    
    This class represents the column configuration structure used in Ignition
    Perspective table components.
    
    Attributes:
        field (str): The field/column name from the data
        visible (bool): Whether the column is visible
        editable (bool): Whether the column is editable
        render (str): Render type - "auto", "number", "date", "boolean", "string", "view"
        justify (str): Horizontal justify - "auto", "left", "center", "right"
        align (str): Vertical align - "top", "center", "bottom"
        resizable (bool): Whether the column is resizable
        sortable (bool): Whether the column is sortable
        sort (str): Sort direction - "none", "ascending", "descending"
        filter (dict): Filter configuration
        viewPath (str): Path to embedded view (when render="view")
        viewParams (dict): Parameters for embedded view
        boolean (str): Boolean display type - "value", "checkbox", "toggle"
        number (str): Number display type - "value", "progress"
        progressBar (dict): Progress bar configuration
        toggleSwitch (dict): Toggle switch configuration
        nullFormat (dict): Null value formatting configuration
        numberFormat (str): Number format string
        dateFormat (str): Date format string
        width (int): Column width in pixels
        strictWidth (bool): Whether to enforce strict width
        style (dict): Style configuration
        header (dict): Header configuration
        footer (dict): Footer configuration
    """
    
    # Available options for various properties
    RENDER_OPTIONS = ("auto", "number", "date", "boolean", "string", "view")
    JUSTIFY_OPTIONS = ("auto", "left", "center", "right")
    ALIGN_OPTIONS = ("top", "center", "bottom")
    SORT_OPTIONS = ("none", "ascending", "descending")
    BOOLEAN_OPTIONS = ("value", "checkbox", "toggle")
    NUMBER_OPTIONS = ("value", "progress")
    NULL_FORMAT_OPTIONS = ("blank", "N/A", None)
    DATE_FORMAT_OPTIONS = ("MM/DD/YYYY", "MM/DD/YYYY HH:mm:ss")
    
    def __init__(self, field=""):
        """
        Initialize a PerspectiveColumnProps instance.
        
        Args:
            field (str): The field/column name from the data
        """
        self._field = field
        self._visible = true
        self._editable = false
        self._render = "auto"
        self._justify = "auto"
        self._align = "center"
        self._resizable = true
        self._sortable = true
        self._sort = "none"
        self._filter = {
            "enabled": false,
            "visible": "on-hover",
            "string": {
                "condition": "",
                "value": ""
            },
            "number": {
                "condition": "",
                "value": ""
            },
            "boolean": {
                "condition": ""
            },
            "date": {
                "condition": "",
                "value": ""
            }
        }
        self._viewPath = ""
        self._viewParams = {}
        self._boolean = "checkbox"
        self._number = "value"
        self._progressBar = {
            "max": 100,
            "min": 0,
            "bar": {
                "color": "",
                "style": {
                    "classes": ""
                }
            },
            "track": {
                "color": "",
                "style": {
                    "classes": ""
                }
            },
            "value": {
                "enabled": true,
                "format": "0,0.##",
                "justify": "center",
                "style": {
                    "classes": ""
                }
            }
        }
        self._toggleSwitch = {
            "color": {
                "selected": "",
                "unselected": ""
            }
        }
        self._nullFormat = {
            "includeNullStrings": false,
            "strict": false,
            "nullFormatValue": ""
        }
        self._numberFormat = "0,0.##"
        self._dateFormat = "MM/DD/YYYY"
        self._width = 200
        self._strictWidth = false
        self._style = {
            "classes": ""
        }
        self._header = {
            "title": "",
            "justify": "left",
            "align": "center",
            "style": {
                "classes": ""
            }
        }
        self._footer = {
            "title": "",
            "justify": "left",
            "align": "center",
            "style": {
                "classes": ""
            }
        }
    
    # Property getters and setters
    @property
    def field(self):
        return self._field
    
    @field.setter
    def field(self, value):
        self._field = value
    
    @property
    def visible(self):
        return self._visible
    
    @visible.setter
    def visible(self, value):
        if not isinstance(value, bool):
            raise ValueError("visible must be a boolean")
        self._visible = value
    
    @property
    def editable(self):
        return self._editable
    
    @editable.setter
    def editable(self, value):
        if not isinstance(value, bool):
            raise ValueError("editable must be a boolean")
        self._editable = value
    
    @property
    def render(self):
        return self._render
    
    @render.setter
    def render(self, value):
        if value not in self.RENDER_OPTIONS:
            raise ValueError("render must be one of: {}".format(self.RENDER_OPTIONS))
        self._render = value
    
    @property
    def justify(self):
        return self._justify
    
    @justify.setter
    def justify(self, value):
        if value not in self.JUSTIFY_OPTIONS:
            raise ValueError("justify must be one of: {}".format(self.JUSTIFY_OPTIONS))
        self._justify = value
    
    @property
    def align(self):
        return self._align
    
    @align.setter
    def align(self, value):
        if value not in self.ALIGN_OPTIONS:
            raise ValueError("align must be one of: {}".format(self.ALIGN_OPTIONS))
        self._align = value
    
    @property
    def resizable(self):
        return self._resizable
    
    @resizable.setter
    def resizable(self, value):
        if not isinstance(value, bool):
            raise ValueError("resizable must be a boolean")
        self._resizable = value
    
    @property
    def sortable(self):
        return self._sortable
    
    @sortable.setter
    def sortable(self, value):
        if not isinstance(value, bool):
            raise ValueError("sortable must be a boolean")
        self._sortable = value
    
    @property
    def sort(self):
        return self._sort
    
    @sort.setter
    def sort(self, value):
        if value not in self.SORT_OPTIONS:
            raise ValueError("sort must be one of: {}".format(self.SORT_OPTIONS))
        self._sort = value
    
    @property
    def filter(self):
        return self._filter
    
    @filter.setter
    def filter(self, value):
        self._filter = value
    
    @property
    def viewPath(self):
        return self._viewPath
    
    @viewPath.setter
    def viewPath(self, value):
        self._viewPath = value
    
    @property
    def viewParams(self):
        return self._viewParams
    
    @viewParams.setter
    def viewParams(self, value):
        if not isinstance(value, dict):
            raise ValueError("viewParams must be a dictionary")
        self._viewParams = value
    
    @property
    def boolean(self):
        return self._boolean
    
    @boolean.setter
    def boolean(self, value):
        if value not in self.BOOLEAN_OPTIONS:
            raise ValueError("boolean must be one of: {}".format(self.BOOLEAN_OPTIONS))
        self._boolean = value
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, value):
        if value not in self.NUMBER_OPTIONS:
            raise ValueError("number must be one of: {}".format(self.NUMBER_OPTIONS))
        self._number = value
    
    @property
    def progressBar(self):
        return self._progressBar
    
    @progressBar.setter
    def progressBar(self, value):
        self._progressBar = value
    
    @property
    def toggleSwitch(self):
        return self._toggleSwitch
    
    @toggleSwitch.setter
    def toggleSwitch(self, value):
        self._toggleSwitch = value
    
    @property
    def nullFormat(self):
        return self._nullFormat
    
    @nullFormat.setter
    def nullFormat(self, value):
        self._nullFormat = value
    
    @property
    def numberFormat(self):
        return self._numberFormat
    
    @numberFormat.setter
    def numberFormat(self, value):
        self._numberFormat = value
    
    @property
    def dateFormat(self):
        return self._dateFormat
    
    @dateFormat.setter
    def dateFormat(self, value):
        self._dateFormat = value
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
    
    @property
    def strictWidth(self):
        return self._strictWidth
    
    @strictWidth.setter
    def strictWidth(self, value):
        if not isinstance(value, bool):
            raise ValueError("strictWidth must be a boolean")
        self._strictWidth = value
    
    @property
    def style(self):
        return self._style
    
    @style.setter
    def style(self, value):
        self._style = value
    
    @property
    def header(self):
        return self._header
    
    @header.setter
    def header(self, value):
        self._header = value
    
    @property
    def footer(self):
        return self._footer
    
    @footer.setter
    def footer(self, value):
        self._footer = value
    
    # Convenience methods for common property modifications
    def set_visible(self, value):
        """Set column visibility."""
        self.visible = value
        return self
    
    def set_editable(self, value):
        """Set column editability."""
        self.editable = value
        return self
    
    def set_render(self, value):
        """Set render type."""
        self.render = value
        return self
    
    def set_sortable(self, value):
        """Set whether column is sortable."""
        self.sortable = value
        return self
    
    def set_filter_enabled(self, value):
        """Enable or disable filtering for this column."""
        if not isinstance(value, bool):
            raise ValueError("filter.enabled must be a boolean")
        self._filter["enabled"] = value
        return self
    
    def set_view_path(self, value):
        """Set the view path for embedded view rendering."""
        self.viewPath = value
        return self
    
    def set_view_params(self, value):
        """Set parameters for embedded view."""
        self.viewParams = value
        return self
    
    def set_null_format_value(self, value):
        """Set the null format value."""
        self._nullFormat["nullFormatValue"] = value
        return self
    
    def set_header_title(self, value):
        """Set the header title."""
        self._header["title"] = value
        return self
    
    def set_number_format(self, value):
        """Set the number format."""
        self.numberFormat = value
        return self
    
    def set_date_format(self, value):
        """Set the date format."""
        self.dateFormat = value
        return self
    
    def to_dict(self):
        """
        Convert the column properties to a dictionary format.
        
        Returns:
            dict: The column properties as a dictionary
        """
        return {
            "field": self._field,
            "visible": self._visible,
            "editable": self._editable,
            "render": self._render,
            "justify": self._justify,
            "align": self._align,
            "resizable": self._resizable,
            "sortable": self._sortable,
            "sort": self._sort,
            "filter": self._filter,
            "viewPath": self._viewPath,
            "viewParams": self._viewParams,
            "boolean": self._boolean,
            "number": self._number,
            "progressBar": self._progressBar,
            "toggleSwitch": self._toggleSwitch,
            "nullFormat": self._nullFormat,
            "numberFormat": self._numberFormat,
            "dateFormat": self._dateFormat,
            "width": self._width,
            "strictWidth": self._strictWidth,
            "style": self._style,
            "header": self._header,
            "footer": self._footer
        }


class SchemaColumnInformation(PerspectiveColumnProps):
    """
    Class representing a database column with its metadata and UI display name.
    
    Inherits from PerspectiveColumnProps and adds schema-specific metadata.
    
    Schema column names are expected to follow the format: Table__columnName
    
    Attributes:
        table_name (str): The name of the database table
        column_name (str): The name of the column in the database
        ui_display_name (str): The display name shown in the UI header
        data_type (str): The data type of the column
        is_nullable (bool): Whether the column allows null values
        is_primary_key (bool): Whether the column is a primary key
    """
    
    def __init__(self, schema_column_name, ui_display_name=None, data_type=None):
        """
        Initialize a SchemaColumnInformation instance.
        
        Args:
            schema_column_name (str): Column name in format Table__columnName
            ui_display_name (str, optional): Display name for UI header
            data_type (str, optional): Data type of the column
        """
        super(SchemaColumnInformation, self).__init__(field=schema_column_name)
        
        # Parse the schema column name (expected format: Table__columnName)
        parts = schema_column_name.split("__")
        if len(parts) == 2:
            self._table_name = parts[0]
            self._column_name = parts[1]
        else:
            self._table_name = ""
            self._column_name = schema_column_name
        
        # Set UI display name (default to column name if not provided)
        self._ui_display_name = ui_display_name if ui_display_name else self._column_name
        self._header["title"] = self._ui_display_name
        
        # Schema metadata
        self._data_type = data_type
        self._is_nullable = true
        self._is_primary_key = false
        
        # Auto-configure render type based on data type
        if data_type:
            self._configure_render_for_type(data_type)
    
    def _configure_render_for_type(self, data_type):
        """
        Configure render type based on the column's data type.
        
        Args:
            data_type (str): The data type of the column
        """
        data_type_lower = data_type.lower() if data_type else ""
        
        if "int" in data_type_lower or "float" in data_type_lower or "decimal" in data_type_lower or "numeric" in data_type_lower:
            self._render = "number"
        elif "date" in data_type_lower or "time" in data_type_lower:
            self._render = "date"
        elif "bool" in data_type_lower or "bit" in data_type_lower:
            self._render = "boolean"
        else:
            self._render = "auto"
    
    @property
    def table_name(self):
        return self._table_name
    
    @property
    def column_name(self):
        return self._column_name
    
    @property
    def ui_display_name(self):
        return self._ui_display_name
    
    @ui_display_name.setter
    def ui_display_name(self, value):
        self._ui_display_name = value
        self._header["title"] = value
    
    @property
    def data_type(self):
        return self._data_type
    
    @data_type.setter
    def data_type(self, value):
        self._data_type = value
        self._configure_render_for_type(value)
    
    @property
    def is_nullable(self):
        return self._is_nullable
    
    @is_nullable.setter
    def is_nullable(self, value):
        self._is_nullable = value
    
    @property
    def is_primary_key(self):
        return self._is_primary_key
    
    @is_primary_key.setter
    def is_primary_key(self, value):
        self._is_primary_key = value


class TableComponentColumnConfiguration(object):
    """
    Class for building column configurations from table component data.
    
    This class initializes all schema columns from the table component's data
    and builds the column properties configuration.
    
    Attributes:
        table_component: The Ignition Perspective table component reference
        columns (dict): Dictionary of column name to SchemaColumnInformation
    """
    
    def __init__(self, table_component):
        """
        Initialize TableComponentColumnConfiguration.
        
        Args:
            table_component: The Ignition Perspective table component
        """
        self._table_component = table_component
        self._columns = {}
        self._column_metadata = {}
        
        # Initialize columns from table data
        self._init_columns()
    
    def _init_columns(self):
        """
        Initialize columns from the table component's data.
        
        Extracts column names from table.props.data and creates
        SchemaColumnInformation instances for each.
        """
        data = self._get_table_data()
        
        if data and len(data) > 0:
            # Get column names from the first row's keys
            first_row = data[0]
            if isinstance(first_row, dict):
                for column_name in first_row.keys():
                    # Create SchemaColumnInformation for each column
                    ui_name = self._column_metadata.get(column_name, {}).get("ui_display_name")
                    data_type = self._column_metadata.get(column_name, {}).get("data_type")
                    
                    column_info = SchemaColumnInformation(
                        schema_column_name=column_name,
                        ui_display_name=ui_name,
                        data_type=data_type
                    )
                    self._columns[column_name] = column_info
    
    def _get_table_data(self):
        """
        Get the table data from the component.
        
        Returns:
            list: The table data as a list of dictionaries
        """
        try:
            # Try to access props.data from the table component
            if hasattr(self._table_component, 'props'):
                props = self._table_component.props
                if hasattr(props, 'data'):
                    return props.data
            # Fallback for direct data access
            elif hasattr(self._table_component, 'data'):
                return self._table_component.data
            # If table_component is already a list (data)
            elif isinstance(self._table_component, list):
                return self._table_component
        except Exception:
            pass
        return []
    
    def get_column(self, column_name):
        """
        Get a specific column configuration by name.
        
        Args:
            column_name (str): The column name (Table__columnName format)
            
        Returns:
            SchemaColumnInformation: The column configuration, or None if not found
        """
        return self._columns.get(column_name)
    
    def set_column_visible(self, column_name, value):
        """
        Set visibility for a specific column.
        
        Args:
            column_name (str): The column name
            value (bool): Visibility value
        """
        column = self.get_column(column_name)
        if column:
            column.set_visible(value)
        return self
    
    def set_column_editable(self, column_name, value):
        """
        Set editability for a specific column.
        
        Args:
            column_name (str): The column name
            value (bool): Editable value
        """
        column = self.get_column(column_name)
        if column:
            column.set_editable(value)
        return self
    
    def set_column_render(self, column_name, value):
        """
        Set render type for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): Render type
        """
        column = self.get_column(column_name)
        if column:
            column.set_render(value)
        return self
    
    def set_column_sortable(self, column_name, value):
        """
        Set sortability for a specific column.
        
        Args:
            column_name (str): The column name
            value (bool): Sortable value
        """
        column = self.get_column(column_name)
        if column:
            column.set_sortable(value)
        return self
    
    def set_column_filter_enabled(self, column_name, value):
        """
        Set filter enabled for a specific column.
        
        Args:
            column_name (str): The column name
            value (bool): Filter enabled value
        """
        column = self.get_column(column_name)
        if column:
            column.set_filter_enabled(value)
        return self
    
    def set_column_view_path(self, column_name, value):
        """
        Set view path for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): View path
        """
        column = self.get_column(column_name)
        if column:
            column.set_view_path(value)
        return self
    
    def set_column_view_params(self, column_name, value):
        """
        Set view params for a specific column.
        
        Args:
            column_name (str): The column name
            value (dict): View parameters
        """
        column = self.get_column(column_name)
        if column:
            column.set_view_params(value)
        return self
    
    def set_column_null_format_value(self, column_name, value):
        """
        Set null format value for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): Null format value
        """
        column = self.get_column(column_name)
        if column:
            column.set_null_format_value(value)
        return self
    
    def set_column_header_title(self, column_name, value):
        """
        Set header title for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): Header title
        """
        column = self.get_column(column_name)
        if column:
            column.set_header_title(value)
        return self
    
    def set_column_number_format(self, column_name, value):
        """
        Set number format for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): Number format
        """
        column = self.get_column(column_name)
        if column:
            column.set_number_format(value)
        return self
    
    def set_column_date_format(self, column_name, value):
        """
        Set date format for a specific column.
        
        Args:
            column_name (str): The column name
            value (str): Date format
        """
        column = self.get_column(column_name)
        if column:
            column.set_date_format(value)
        return self
    
    def build_columns(self):
        """
        Build and return the column configurations as a list of dictionaries.
        
        Returns:
            list: List of column property dictionaries [{}, {}]
        """
        columns_list = []
        for column_name in self._columns:
            column_info = self._columns[column_name]
            columns_list.append(column_info.to_dict())
        return columns_list
    
    def apply_to_table(self):
        """
        Apply the column configurations to the table component.
        
        This method sets the table.props.columns property with the
        built column configurations.
        """
        columns_config = self.build_columns()
        
        try:
            if hasattr(self._table_component, 'props'):
                self._table_component.props.columns = columns_config
            elif hasattr(self._table_component, 'columns'):
                self._table_component.columns = columns_config
        except Exception:
            pass
        
        return columns_config
    
    @property
    def columns(self):
        """Get all column configurations."""
        return self._columns


class ViewRobotDetails(TableComponentColumnConfiguration):
    """
    Example subclass for RobotDetails view configuration.
    
    This class demonstrates how to create view-specific column
    configurations by extending TableComponentColumnConfiguration.
    
    Usage in Ignition change script:
        if len(table.props.data) > 0:
            table_component = self
            ViewRobotDetails(table_component)
    """
    
    def __init__(self, table_component):
        """
        Initialize ViewRobotDetails configuration.
        
        Args:
            table_component: The Ignition Perspective table component
        """
        super(ViewRobotDetails, self).__init__(table_component)
        
        # Apply view-specific configurations
        self._configure_columns()
        
        # Automatically apply to table
        self.apply_to_table()
    
    def _configure_columns(self):
        """
        Configure columns specific to the RobotDetails view.
        
        Override this method in subclasses to provide custom
        column configurations.
        """
        # Example configurations - these can be customized based on actual requirements
        pass
    
    def configure_column(self, column_name):
        """
        Get a column configuration builder for fluent configuration.
        
        Args:
            column_name (str): The column name to configure
            
        Returns:
            ColumnConfigurator: A fluent configurator for the column
        """
        return ColumnConfigurator(self, column_name)


class ColumnConfigurator(object):
    """
    Fluent API for configuring individual columns.
    
    This class provides a fluent interface for chaining column
    configuration method calls.
    """
    
    def __init__(self, table_config, column_name):
        """
        Initialize ColumnConfigurator.
        
        Args:
            table_config (TableComponentColumnConfiguration): The parent configuration
            column_name (str): The column name to configure
        """
        self._table_config = table_config
        self._column_name = column_name
    
    def visible(self, value):
        """Set visibility."""
        self._table_config.set_column_visible(self._column_name, value)
        return self
    
    def editable(self, value):
        """Set editability."""
        self._table_config.set_column_editable(self._column_name, value)
        return self
    
    def render(self, value):
        """Set render type."""
        self._table_config.set_column_render(self._column_name, value)
        return self
    
    def sortable(self, value):
        """Set sortability."""
        self._table_config.set_column_sortable(self._column_name, value)
        return self
    
    def filter_enabled(self, value):
        """Set filter enabled."""
        self._table_config.set_column_filter_enabled(self._column_name, value)
        return self
    
    def view_path(self, value):
        """Set view path."""
        self._table_config.set_column_view_path(self._column_name, value)
        return self
    
    def view_params(self, value):
        """Set view params."""
        self._table_config.set_column_view_params(self._column_name, value)
        return self
    
    def null_format_value(self, value):
        """Set null format value."""
        self._table_config.set_column_null_format_value(self._column_name, value)
        return self
    
    def header_title(self, value):
        """Set header title."""
        self._table_config.set_column_header_title(self._column_name, value)
        return self
    
    def number_format(self, value):
        """Set number format."""
        self._table_config.set_column_number_format(self._column_name, value)
        return self
    
    def date_format(self, value):
        """Set date format."""
        self._table_config.set_column_date_format(self._column_name, value)
        return self
    
    def done(self):
        """Return to the parent configuration."""
        return self._table_config
