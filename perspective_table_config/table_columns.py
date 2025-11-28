"""
Table Columns Builder Module

Provides a class for building complete table column configurations
from data sources for Ignition Perspective Table components.
"""

from typing import Any, Dict, List, Optional, Callable, Union
from .column_builder import ColumnBuilder, ColumnConfig


class TableColumnsBuilder:
    """
    Builder for creating complete table column configurations.
    
    This class provides methods for dynamically generating column
    configurations based on data structure and custom rules.
    """
    
    # Type mapping for automatic column type detection
    TYPE_MAPPINGS: Dict[str, Callable[[str, Optional[str]], ColumnConfig]] = {}
    
    def __init__(self):
        """Initialize the table columns builder."""
        self._columns: List[ColumnConfig] = []
        self._type_rules: Dict[str, Callable[[str, Optional[str]], ColumnConfig]] = {}
        self._default_settings: Dict[str, Any] = {}
        self._field_overrides: Dict[str, ColumnConfig] = {}
        self._excluded_fields: set = set()
        
        # Initialize default type rules
        self._init_default_type_rules()
    
    def _init_default_type_rules(self) -> None:
        """Initialize default rules for detecting column types from field names."""
        # Date/time fields
        self._type_rules["date"] = lambda f, t: ColumnBuilder.date(f, t)
        self._type_rules["time"] = lambda f, t: ColumnBuilder.datetime(f, t)
        self._type_rules["timestamp"] = lambda f, t: ColumnBuilder.datetime(f, t)
        self._type_rules["created"] = lambda f, t: ColumnBuilder.datetime(f, t)
        self._type_rules["updated"] = lambda f, t: ColumnBuilder.datetime(f, t)
        self._type_rules["modified"] = lambda f, t: ColumnBuilder.datetime(f, t)
        
        # Boolean fields
        self._type_rules["is_"] = lambda f, t: ColumnBuilder.boolean(f, t)
        self._type_rules["has_"] = lambda f, t: ColumnBuilder.boolean(f, t)
        self._type_rules["active"] = lambda f, t: ColumnBuilder.boolean(f, t)
        self._type_rules["enabled"] = lambda f, t: ColumnBuilder.boolean(f, t)
        self._type_rules["visible"] = lambda f, t: ColumnBuilder.boolean(f, t)
        
        # ID fields
        self._type_rules["_id"] = lambda f, t: ColumnBuilder.id_column(f, t or "ID")
        
        # Currency/money fields
        self._type_rules["price"] = lambda f, t: ColumnBuilder.currency(f, t)
        self._type_rules["cost"] = lambda f, t: ColumnBuilder.currency(f, t)
        self._type_rules["amount"] = lambda f, t: ColumnBuilder.currency(f, t)
        self._type_rules["total"] = lambda f, t: ColumnBuilder.currency(f, t)
        self._type_rules["balance"] = lambda f, t: ColumnBuilder.currency(f, t)
        
        # Percentage/progress fields
        self._type_rules["percent"] = lambda f, t: ColumnBuilder.progress(f, t)
        self._type_rules["progress"] = lambda f, t: ColumnBuilder.progress(f, t)
        self._type_rules["completion"] = lambda f, t: ColumnBuilder.progress(f, t)
    
    def add_type_rule(
        self,
        pattern: str,
        column_factory: Callable[[str, Optional[str]], ColumnConfig]
    ) -> "TableColumnsBuilder":
        """
        Add a custom type rule for column detection.
        
        Args:
            pattern: Pattern to match in field names (case-insensitive)
            column_factory: Factory function that creates a ColumnConfig
            
        Returns:
            self for method chaining
        """
        self._type_rules[pattern.lower()] = column_factory
        return self
    
    def set_default_settings(
        self,
        sortable: Optional[bool] = None,
        editable: Optional[bool] = None,
        resizable: Optional[bool] = None,
        width: Optional[int] = None
    ) -> "TableColumnsBuilder":
        """
        Set default settings to apply to all columns.
        
        Args:
            sortable: Default sortable setting
            editable: Default editable setting
            resizable: Default resizable setting
            width: Default width
            
        Returns:
            self for method chaining
        """
        if sortable is not None:
            self._default_settings["sortable"] = sortable
        if editable is not None:
            self._default_settings["editable"] = editable
        if resizable is not None:
            self._default_settings["resizable"] = resizable
        if width is not None:
            self._default_settings["width"] = width
        return self
    
    def exclude_fields(self, *fields: str) -> "TableColumnsBuilder":
        """
        Exclude specific fields from column generation.
        
        Args:
            *fields: Field names to exclude
            
        Returns:
            self for method chaining
        """
        self._excluded_fields.update(fields)
        return self
    
    def add_field_override(
        self,
        field: str,
        config: ColumnConfig
    ) -> "TableColumnsBuilder":
        """
        Add a custom column configuration for a specific field.
        
        Args:
            field: Field name to override
            config: Custom column configuration
            
        Returns:
            self for method chaining
        """
        self._field_overrides[field] = config
        return self
    
    def add_column(self, config: ColumnConfig) -> "TableColumnsBuilder":
        """
        Add a column configuration directly.
        
        Args:
            config: Column configuration to add
            
        Returns:
            self for method chaining
        """
        self._columns.append(config)
        return self
    
    def _detect_column_type(self, field: str) -> Optional[ColumnConfig]:
        """
        Detect the appropriate column type based on field name.
        
        Args:
            field: Field name to analyze
            
        Returns:
            ColumnConfig if a matching rule is found, None otherwise
        """
        field_lower = field.lower()
        
        # Check for exact matches first
        for pattern, factory in self._type_rules.items():
            if field_lower == pattern:
                return factory(field, self._humanize_field_name(field))
        
        # Check for prefix/suffix matches
        for pattern, factory in self._type_rules.items():
            if field_lower.startswith(pattern) or field_lower.endswith(pattern):
                return factory(field, self._humanize_field_name(field))
            if pattern in field_lower:
                return factory(field, self._humanize_field_name(field))
        
        return None
    
    def _humanize_field_name(self, field: str) -> str:
        """
        Convert a field name to a human-readable title.
        
        Args:
            field: Field name to humanize
            
        Returns:
            Human-readable title
        """
        # Handle camelCase
        import re
        result = re.sub(r'([a-z])([A-Z])', r'\1 \2', field)
        # Handle snake_case
        result = result.replace('_', ' ')
        # Handle kebab-case
        result = result.replace('-', ' ')
        # Title case
        return result.title()
    
    def from_field_list(
        self,
        fields: List[str],
        include_unknown: bool = True
    ) -> "TableColumnsBuilder":
        """
        Generate column configurations from a list of field names.
        
        Args:
            fields: List of field names
            include_unknown: Whether to include fields that don't match any rule
            
        Returns:
            self for method chaining
        """
        for field in fields:
            if field in self._excluded_fields:
                continue
                
            # Check for overrides
            if field in self._field_overrides:
                self._columns.append(self._field_overrides[field])
                continue
            
            # Try to detect column type
            config = self._detect_column_type(field)
            if config is None and include_unknown:
                config = ColumnBuilder.text(field, self._humanize_field_name(field))
            
            if config is not None:
                # Apply default settings
                if "sortable" in self._default_settings:
                    config.sortable(self._default_settings["sortable"])
                if "editable" in self._default_settings:
                    config.editable(self._default_settings["editable"])
                if "resizable" in self._default_settings:
                    config.resizable(self._default_settings["resizable"])
                if "width" in self._default_settings:
                    config.width(value=self._default_settings["width"])
                    
                self._columns.append(config)
        
        return self
    
    def from_data(
        self,
        data: Union[List[Dict[str, Any]], Dict[str, Any]],
        include_unknown: bool = True
    ) -> "TableColumnsBuilder":
        """
        Generate column configurations from sample data.
        
        Args:
            data: Sample data (list of dicts or single dict)
            include_unknown: Whether to include fields that don't match any rule
            
        Returns:
            self for method chaining
        """
        if isinstance(data, list):
            if len(data) == 0:
                return self
            sample = data[0]
        else:
            sample = data
            
        if not isinstance(sample, dict):
            return self
            
        fields = list(sample.keys())
        return self.from_field_list(fields, include_unknown)
    
    def from_dataset_columns(
        self,
        dataset: Any,
        include_unknown: bool = True
    ) -> "TableColumnsBuilder":
        """
        Generate column configurations from an Ignition dataset.
        
        This method works with Ignition's dataset objects and extracts
        column names using the getColumnNames() method.
        
        Args:
            dataset: An Ignition dataset object
            include_unknown: Whether to include fields that don't match any rule
            
        Returns:
            self for method chaining
        """
        try:
            # Try to get column names from Ignition dataset
            if hasattr(dataset, 'getColumnNames'):
                fields = list(dataset.getColumnNames())
            elif hasattr(dataset, 'columnNames'):
                fields = list(dataset.columnNames)
            elif hasattr(dataset, 'getColumnCount'):
                # Fallback: iterate through column indices
                fields = []
                for i in range(dataset.getColumnCount()):
                    if hasattr(dataset, 'getColumnName'):
                        fields.append(dataset.getColumnName(i))
            else:
                # Last resort: try to iterate as if it's a list of dicts
                return self.from_data(dataset, include_unknown)
                
            return self.from_field_list(fields, include_unknown)
        except Exception:
            return self
    
    def reorder(self, *fields: str) -> "TableColumnsBuilder":
        """
        Reorder columns to put specified fields first.
        
        Args:
            *fields: Field names in the desired order
            
        Returns:
            self for method chaining
        """
        # Create ordered list of columns
        ordered_columns: List[ColumnConfig] = []
        remaining_columns = list(self._columns)
        
        for field in fields:
            for col in remaining_columns[:]:
                col_dict = col.build()
                if col_dict.get("field") == field:
                    ordered_columns.append(col)
                    remaining_columns.remove(col)
                    break
        
        # Add remaining columns at the end
        ordered_columns.extend(remaining_columns)
        self._columns = ordered_columns
        
        return self
    
    def clear(self) -> "TableColumnsBuilder":
        """
        Clear all columns.
        
        Returns:
            self for method chaining
        """
        self._columns = []
        return self
    
    def build(self) -> List[Dict[str, Any]]:
        """
        Build and return the complete list of column configurations.
        
        Returns:
            List of column configuration dictionaries
        """
        return [col.build() for col in self._columns]
    
    def build_json(self, indent: int = 2) -> str:
        """
        Build and return the column configurations as a JSON string.
        
        Args:
            indent: JSON indentation level
            
        Returns:
            JSON string representation of columns
        """
        import json
        return json.dumps(self.build(), indent=indent)


def build_columns_from_data(
    data: Union[List[Dict[str, Any]], Dict[str, Any]],
    exclude_fields: Optional[List[str]] = None,
    field_overrides: Optional[Dict[str, ColumnConfig]] = None,
    sortable: bool = True,
    editable: bool = False
) -> List[Dict[str, Any]]:
    """
    Convenience function to quickly build columns from data.
    
    Args:
        data: Sample data to generate columns from
        exclude_fields: Fields to exclude from generation
        field_overrides: Custom column configurations for specific fields
        sortable: Whether columns should be sortable by default
        editable: Whether columns should be editable by default
        
    Returns:
        List of column configuration dictionaries
    """
    builder = TableColumnsBuilder()
    builder.set_default_settings(sortable=sortable, editable=editable)
    
    if exclude_fields:
        builder.exclude_fields(*exclude_fields)
    
    if field_overrides:
        for field, config in field_overrides.items():
            builder.add_field_override(field, config)
    
    return builder.from_data(data).build()


def build_columns_from_fields(
    fields: List[str],
    exclude_fields: Optional[List[str]] = None,
    field_overrides: Optional[Dict[str, ColumnConfig]] = None,
    sortable: bool = True,
    editable: bool = False
) -> List[Dict[str, Any]]:
    """
    Convenience function to quickly build columns from field names.
    
    Args:
        fields: List of field names
        exclude_fields: Fields to exclude from generation
        field_overrides: Custom column configurations for specific fields
        sortable: Whether columns should be sortable by default
        editable: Whether columns should be editable by default
        
    Returns:
        List of column configuration dictionaries
    """
    builder = TableColumnsBuilder()
    builder.set_default_settings(sortable=sortable, editable=editable)
    
    if exclude_fields:
        builder.exclude_fields(*exclude_fields)
    
    if field_overrides:
        for field, config in field_overrides.items():
            builder.add_field_override(field, config)
    
    return builder.from_field_list(fields).build()
