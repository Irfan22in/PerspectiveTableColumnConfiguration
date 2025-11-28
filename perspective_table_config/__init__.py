"""
Perspective Table Column Configuration Builder

A Python module for dynamically building column configurations for
Ignition Perspective Table components.
"""

from .column_builder import ColumnBuilder, ColumnConfig
from .table_columns import TableColumnsBuilder

__version__ = "1.0.0"
__all__ = ["ColumnBuilder", "ColumnConfig", "TableColumnsBuilder"]
