# -*- coding: utf-8 -*-
"""
TableComponentColumnConfiguration class for Ignition Perspective Table column configuration.

This module contains the TableComponentColumnConfiguration class that builds 
table column configurations dynamically based on table component data.
"""

from schema_column_information import SchemaColumnInformation


class TableComponentColumnConfiguration(object):
    """
    Class for building table column configurations dynamically.
    
    This class initializes all schema columns from the table component data
    and builds column properties in the form of [{}, {}].
    """
    
    def __init__(self, table_component):
        """
        Initialize a TableComponentColumnConfiguration instance.
        
        Args:
            table_component: The Ignition Perspective table component reference.
                             Expected to have props.data as list of dictionaries.
        """
        self.table_component = table_component
        self.columns = {}
        self._initialize_columns()
    
    def _initialize_columns(self):
        """
        Initialize columns from the table component data.
        
        Extracts column names from the first row of data and creates
        SchemaColumnInformation instances for each column.
        """
        data = self._get_table_data()
        
        if data and len(data) > 0:
            # Get column names from the first row keys
            first_row = data[0]
            for column_name in first_row.keys():
                self.columns[column_name] = SchemaColumnInformation(column_name)
    
    def _get_table_data(self):
        """
        Get the data from the table component.
        
        Returns:
            list: The table data as a list of dictionaries
        """
        try:
            return self.table_component.props.data
        except AttributeError:
            return []
    
    def get_column(self, column_name):
        """
        Get a specific column configuration by name.
        
        Args:
            column_name (str): The name of the column
        
        Returns:
            SchemaColumnInformation: The column configuration, or None if not found
        """
        return self.columns.get(column_name)
    
    def set_column_visible(self, column_name, visible):
        """
        Set the visibility for a specific column.
        
        Args:
            column_name (str): The name of the column
            visible (bool): Whether the column should be visible
        """
        if column_name in self.columns:
            self.columns[column_name].set_visible(visible)
        return self
    
    def set_column_editable(self, column_name, editable):
        """
        Set whether a specific column is editable.
        
        Args:
            column_name (str): The name of the column
            editable (bool): Whether the column should be editable
        """
        if column_name in self.columns:
            self.columns[column_name].set_editable(editable)
        return self
    
    def set_column_render(self, column_name, render):
        """
        Set the render type for a specific column.
        
        Args:
            column_name (str): The name of the column
            render (str): The render type
        """
        if column_name in self.columns:
            self.columns[column_name].set_render(render)
        return self
    
    def set_column_sortable(self, column_name, sortable):
        """
        Set whether a specific column is sortable.
        
        Args:
            column_name (str): The name of the column
            sortable (bool): Whether the column should be sortable
        """
        if column_name in self.columns:
            self.columns[column_name].set_sortable(sortable)
        return self
    
    def set_column_filter_enabled(self, column_name, enabled):
        """
        Set whether filtering is enabled for a specific column.
        
        Args:
            column_name (str): The name of the column
            enabled (bool): Whether filtering should be enabled
        """
        if column_name in self.columns:
            self.columns[column_name].set_filter_enabled(enabled)
        return self
    
    def set_column_view_path(self, column_name, view_path):
        """
        Set the view path for a specific column.
        
        Args:
            column_name (str): The name of the column
            view_path (str): The path to the view
        """
        if column_name in self.columns:
            self.columns[column_name].set_view_path(view_path)
        return self
    
    def set_column_view_params(self, column_name, view_params):
        """
        Set the view parameters for a specific column.
        
        Args:
            column_name (str): The name of the column
            view_params (dict): Parameters to pass to the view
        """
        if column_name in self.columns:
            self.columns[column_name].set_view_params(view_params)
        return self
    
    def set_column_null_format_value(self, column_name, value):
        """
        Set the null format value for a specific column.
        
        Args:
            column_name (str): The name of the column
            value (str): The null format value
        """
        if column_name in self.columns:
            self.columns[column_name].set_null_format_value(value)
        return self
    
    def set_column_header_title(self, column_name, title):
        """
        Set the header title for a specific column.
        
        Args:
            column_name (str): The name of the column
            title (str): The header title
        """
        if column_name in self.columns:
            self.columns[column_name].set_header_title(title)
        return self
    
    def set_column_number_format(self, column_name, format_string):
        """
        Set the number format for a specific column.
        
        Args:
            column_name (str): The name of the column
            format_string (str): The number format string
        """
        if column_name in self.columns:
            self.columns[column_name].set_number_format(format_string)
        return self
    
    def set_column_date_format(self, column_name, format_string):
        """
        Set the date format for a specific column.
        
        Args:
            column_name (str): The name of the column
            format_string (str): The date format string
        """
        if column_name in self.columns:
            self.columns[column_name].set_date_format(format_string)
        return self
    
    def build_columns(self):
        """
        Build the column configurations as a list of dictionaries.
        
        Returns:
            list: A list of column property dictionaries [{}, {}]
        """
        return [col.to_dict() for col in self.columns.values()]
    
    def apply_to_table(self):
        """
        Apply the built column configurations to the table component.
        
        Sets the table.props.columns property with the built column configurations.
        """
        try:
            self.table_component.props.columns = self.build_columns()
        except AttributeError:
            pass
        return self


class ViewRobotDetails(TableComponentColumnConfiguration):
    """
    Example subclass for the RobotDetails view.
    
    This class demonstrates how to create a view-specific configuration
    that inherits from TableComponentColumnConfiguration.
    """
    
    def __init__(self, table_component):
        """
        Initialize a ViewRobotDetails instance.
        
        Args:
            table_component: The Ignition Perspective table component reference.
        """
        super(ViewRobotDetails, self).__init__(table_component)
        
        # Apply view-specific column configurations here
        self._configure_columns()
    
    def _configure_columns(self):
        """
        Configure columns specific to the RobotDetails view.
        
        Override this method in subclasses to apply view-specific configurations.
        """
        # Example: Configure specific columns for RobotDetails view
        # This method can be overridden to set specific properties
        pass
