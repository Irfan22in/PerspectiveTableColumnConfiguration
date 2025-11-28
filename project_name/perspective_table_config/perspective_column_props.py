# -*- coding: utf-8 -*-
"""
PerspectiveColumnProps class for Ignition Perspective Table column configuration.

This module contains the PerspectiveColumnProps class that has all attributes 
of an Ignition Perspective table column.
"""

class PerspectiveColumnProps(object):
    """
    Class representing all properties of an Ignition Perspective table column.
    
    Provides methods to configure visibility, editability, rendering, sorting,
    filtering, view paths, and formatting options for table columns.
    """
    
    # Available options for render
    RENDER_OPTIONS = ["auto", "number", "date", "boolean", "string", "view"]
    
    # Available options for justify
    JUSTIFY_OPTIONS = ["auto", "left", "center", "right"]
    
    # Available options for align
    ALIGN_OPTIONS = ["top", "center", "bottom"]
    
    # Available options for sort
    SORT_OPTIONS = ["none", "ascending", "descending"]
    
    # Available options for boolean display
    BOOLEAN_OPTIONS = ["value", "checkbox", "toggle"]
    
    # Available options for number display
    NUMBER_OPTIONS = ["value", "progress"]
    
    # Available options for null format value
    NULL_FORMAT_OPTIONS = ["blank", "N/A", None]
    
    # Available options for date format
    DATE_FORMAT_OPTIONS = ["MM/DD/YYYY", "MM/DD/YYYY HH:mm:ss"]
    
    def __init__(self, field):
        """
        Initialize a PerspectiveColumnProps instance.
        
        Args:
            field (str): The field name for the column (e.g., "table_columnName")
        """
        self.field = field
        self.visible = True
        self.editable = False
        self.render = "auto"
        self.justify = "auto"
        self.align = "center"
        self.resizable = True
        self.sortable = True
        self.sort = "none"
        self.filter = {
            "enabled": False,
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
        self.viewPath = ""
        self.viewParams = {}
        self.boolean = "checkbox"
        self.number = "value"
        self.progressBar = {
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
                "enabled": True,
                "format": "0,0.##",
                "justify": "center",
                "style": {
                    "classes": ""
                }
            }
        }
        self.toggleSwitch = {
            "color": {
                "selected": "",
                "unselected": ""
            }
        }
        self.nullFormat = {
            "includeNullStrings": False,
            "strict": False,
            "nullFormatValue": ""
        }
        self.numberFormat = "0,0.##"
        self.dateFormat = "MM/DD/YYYY"
        self.width = 200
        self.strictWidth = False
        self.style = {
            "classes": ""
        }
        self.header = {
            "title": "",
            "justify": "left",
            "align": "center",
            "style": {
                "classes": ""
            }
        }
        self.footer = {
            "title": "",
            "justify": "left",
            "align": "center",
            "style": {
                "classes": ""
            }
        }
    
    def set_visible(self, visible):
        """
        Set the visibility of the column.
        
        Args:
            visible (bool): Whether the column is visible
        """
        self.visible = visible
        return self
    
    def set_editable(self, editable):
        """
        Set whether the column is editable.
        
        Args:
            editable (bool): Whether the column is editable
        """
        self.editable = editable
        return self
    
    def set_render(self, render):
        """
        Set the render type for the column.
        
        Args:
            render (str): Render type. Options: "auto", "number", "date", "boolean", "string", "view"
        """
        if render in self.RENDER_OPTIONS:
            self.render = render
        return self
    
    def set_sortable(self, sortable):
        """
        Set whether the column is sortable.
        
        Args:
            sortable (bool): Whether the column is sortable
        """
        self.sortable = sortable
        return self
    
    def set_filter_enabled(self, enabled):
        """
        Set whether filtering is enabled for the column.
        
        Args:
            enabled (bool): Whether filtering is enabled
        """
        self.filter["enabled"] = enabled
        return self
    
    def set_view_path(self, view_path):
        """
        Set the view path for the column (used when render is "view").
        
        Args:
            view_path (str): The path to the view
        """
        self.viewPath = view_path
        return self
    
    def set_view_params(self, view_params):
        """
        Set the view parameters for the column.
        
        Args:
            view_params (dict): Parameters to pass to the view
        """
        self.viewParams = view_params
        return self
    
    def set_null_format_value(self, value):
        """
        Set the null format value.
        
        Args:
            value (str): Null format value. Options: "blank", "N/A", None
        """
        self.nullFormat["nullFormatValue"] = value
        return self
    
    def set_header_title(self, title):
        """
        Set the header title for the column.
        
        Args:
            title (str): The display title for the column header
        """
        self.header["title"] = title
        return self
    
    def set_number_format(self, format_string):
        """
        Set the number format for the column.
        
        Args:
            format_string (str): The number format string (e.g., "0,0.##")
        """
        self.numberFormat = format_string
        return self
    
    def set_date_format(self, format_string):
        """
        Set the date format for the column.
        
        Args:
            format_string (str): The date format string. Options: "MM/DD/YYYY", "MM/DD/YYYY HH:mm:ss"
        """
        self.dateFormat = format_string
        return self
    
    def set_width(self, width):
        """
        Set the width of the column.
        
        Args:
            width (int): The width in pixels
        """
        self.width = width
        return self
    
    def to_dict(self):
        """
        Convert the column properties to a dictionary.
        
        Returns:
            dict: A dictionary representation of the column properties
        """
        return {
            "field": self.field,
            "visible": self.visible,
            "editable": self.editable,
            "render": self.render,
            "justify": self.justify,
            "align": self.align,
            "resizable": self.resizable,
            "sortable": self.sortable,
            "sort": self.sort,
            "filter": self.filter,
            "viewPath": self.viewPath,
            "viewParams": self.viewParams,
            "boolean": self.boolean,
            "number": self.number,
            "progressBar": self.progressBar,
            "toggleSwitch": self.toggleSwitch,
            "nullFormat": self.nullFormat,
            "numberFormat": self.numberFormat,
            "dateFormat": self.dateFormat,
            "width": self.width,
            "strictWidth": self.strictWidth,
            "style": self.style,
            "header": self.header,
            "footer": self.footer
        }
