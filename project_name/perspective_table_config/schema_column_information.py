# -*- coding: utf-8 -*-
"""
SchemaColumnInformation class for Ignition Perspective Table column configuration.

This module contains the SchemaColumnInformation class that represents 
each column from the database with its metadata and UI display name.
"""

from perspective_column_props import PerspectiveColumnProps


class SchemaColumnInformation(PerspectiveColumnProps):
    """
    Class representing column information from the database schema.
    
    Inherits from PerspectiveColumnProps and adds metadata mapping functionality.
    Each column from the database is represented with its metadata and UI display name.
    
    The schema column name format is expected to be: Table__columnName
    """
    
    def __init__(self, schema_column_name, ui_display_name=None):
        """
        Initialize a SchemaColumnInformation instance.
        
        Args:
            schema_column_name (str): The schema column name in format "Table__columnName"
            ui_display_name (str, optional): The display name for the UI. 
                                              If not provided, derives from schema_column_name.
        """
        # Initialize parent class with the schema column name as field
        super(SchemaColumnInformation, self).__init__(schema_column_name)
        
        # Store schema column name
        self.schema_column_name = schema_column_name
        
        # Parse table and column name from schema column name
        self.table_name, self.column_name = self._parse_schema_column_name(schema_column_name)
        
        # Set UI display name
        if ui_display_name is not None:
            self.ui_display_name = ui_display_name
        else:
            # Default to column name with underscores replaced by spaces and title cased
            self.ui_display_name = self._format_display_name(self.column_name)
        
        # Set the header title to the UI display name
        self.set_header_title(self.ui_display_name)
    
    def _parse_schema_column_name(self, schema_column_name):
        """
        Parse the schema column name into table and column parts.
        
        Args:
            schema_column_name (str): The schema column name in format "Table__columnName"
        
        Returns:
            tuple: (table_name, column_name)
        """
        if "__" in schema_column_name:
            parts = schema_column_name.split("__", 1)
            return parts[0], parts[1]
        else:
            return "", schema_column_name
    
    def _format_display_name(self, column_name):
        """
        Format a column name into a display-friendly name.
        
        Args:
            column_name (str): The column name to format
        
        Returns:
            str: The formatted display name
        """
        # Replace underscores with spaces and title case
        return column_name.replace("_", " ").title()
    
    def set_ui_display_name(self, display_name):
        """
        Set the UI display name for the column.
        
        Args:
            display_name (str): The display name to set
        """
        self.ui_display_name = display_name
        self.set_header_title(display_name)
        return self
    
    def get_table_name(self):
        """
        Get the table name from the schema column name.
        
        Returns:
            str: The table name
        """
        return self.table_name
    
    def get_column_name(self):
        """
        Get the column name from the schema column name.
        
        Returns:
            str: The column name
        """
        return self.column_name
    
    def to_dict(self):
        """
        Convert the schema column information to a dictionary.
        
        Returns:
            dict: A dictionary representation including metadata
        """
        base_dict = super(SchemaColumnInformation, self).to_dict()
        base_dict["_metadata"] = {
            "schemaColumnName": self.schema_column_name,
            "tableName": self.table_name,
            "columnName": self.column_name,
            "uiDisplayName": self.ui_display_name
        }
        return base_dict
