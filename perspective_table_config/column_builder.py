"""
Column Builder Module

Provides classes for building individual column configurations
for Ignition Perspective Table components.
"""

from typing import Any, Dict, List, Optional, Union


class ColumnConfig:
    """
    Represents a single column configuration for a Perspective Table.
    
    This class provides a fluent interface for building column configurations
    with all the properties supported by the Perspective Table component.
    """
    
    # Render types supported by Perspective Table
    RENDER_AUTO = "auto"
    RENDER_NUMBER = "number"
    RENDER_DATE = "date"
    RENDER_BOOLEAN = "boolean"
    RENDER_STRING = "string"
    RENDER_VIEW = "view"
    RENDER_PROGRESS = "progress"
    RENDER_TOGGLE = "toggle"
    
    # Justify options
    JUSTIFY_LEFT = "left"
    JUSTIFY_CENTER = "center"
    JUSTIFY_RIGHT = "right"
    
    # Sort directions
    SORT_ASC = "asc"
    SORT_DESC = "desc"
    SORT_NONE = "none"
    
    def __init__(self, field: str):
        """
        Initialize a column configuration with a field name.
        
        Args:
            field: The field name from the data source that this column displays
        """
        self._config: Dict[str, Any] = {
            "field": field,
            "visible": True
        }
        self._header: Dict[str, Any] = {"title": field}
        self._render_config: Dict[str, Any] = {}
        self._style: Dict[str, Any] = {}
        self._filter_config: Dict[str, Any] = {}
        
    def header(
        self,
        title: Optional[str] = None,
        tooltip: Optional[str] = None,
        align: Optional[str] = None
    ) -> "ColumnConfig":
        """
        Configure the column header.
        
        Args:
            title: The display title for the column header
            tooltip: Tooltip text to show on hover
            align: Text alignment for the header
            
        Returns:
            self for method chaining
        """
        if title is not None:
            self._header["title"] = title
        if tooltip is not None:
            self._header["tooltip"] = tooltip
        if align is not None:
            self._header["align"] = align
        return self
    
    def width(
        self,
        value: Optional[int] = None,
        min_width: Optional[int] = None,
        max_width: Optional[int] = None,
        grow: Optional[int] = None
    ) -> "ColumnConfig":
        """
        Configure column width settings.
        
        Args:
            value: Fixed width in pixels
            min_width: Minimum width in pixels
            max_width: Maximum width in pixels
            grow: Flex grow factor
            
        Returns:
            self for method chaining
        """
        if value is not None:
            self._config["width"] = value
        if min_width is not None:
            self._config["minWidth"] = min_width
        if max_width is not None:
            self._config["maxWidth"] = max_width
        if grow is not None:
            self._config["grow"] = grow
        return self
    
    def justify(self, value: str) -> "ColumnConfig":
        """
        Set the text justification for the column.
        
        Args:
            value: One of 'left', 'center', or 'right'
            
        Returns:
            self for method chaining
        """
        self._config["justify"] = value
        return self
    
    def visible(self, is_visible: bool = True) -> "ColumnConfig":
        """
        Set column visibility.
        
        Args:
            is_visible: Whether the column should be visible
            
        Returns:
            self for method chaining
        """
        self._config["visible"] = is_visible
        return self
    
    def editable(self, is_editable: bool = True) -> "ColumnConfig":
        """
        Set whether the column is editable.
        
        Args:
            is_editable: Whether cells in this column can be edited
            
        Returns:
            self for method chaining
        """
        self._config["editable"] = is_editable
        return self
    
    def sortable(self, is_sortable: bool = True) -> "ColumnConfig":
        """
        Set whether the column is sortable.
        
        Args:
            is_sortable: Whether the column can be sorted
            
        Returns:
            self for method chaining
        """
        self._config["sortable"] = is_sortable
        return self
    
    def resizable(self, is_resizable: bool = True) -> "ColumnConfig":
        """
        Set whether the column is resizable.
        
        Args:
            is_resizable: Whether the column can be resized by the user
            
        Returns:
            self for method chaining
        """
        self._config["resizable"] = is_resizable
        return self
    
    def render(
        self,
        render_type: str = RENDER_AUTO,
        **options: Any
    ) -> "ColumnConfig":
        """
        Configure the render type and options for the column.
        
        Args:
            render_type: The render type (auto, number, date, boolean, string, view, progress, toggle)
            **options: Additional render options specific to the render type
            
        Returns:
            self for method chaining
        """
        self._config["render"] = render_type
        if options:
            self._render_config.update(options)
        return self
    
    def number_format(
        self,
        format_string: Optional[str] = None,
        use_grouping: bool = True,
        minimum_fraction_digits: Optional[int] = None,
        maximum_fraction_digits: Optional[int] = None
    ) -> "ColumnConfig":
        """
        Configure number formatting for a number column.
        
        Args:
            format_string: Number format pattern (e.g., '0,0.00')
            use_grouping: Whether to use digit grouping (thousands separator)
            minimum_fraction_digits: Minimum number of decimal places
            maximum_fraction_digits: Maximum number of decimal places
            
        Returns:
            self for method chaining
        """
        self._config["render"] = self.RENDER_NUMBER
        number_config: Dict[str, Any] = {}
        if format_string is not None:
            number_config["format"] = format_string
        number_config["useGrouping"] = use_grouping
        if minimum_fraction_digits is not None:
            number_config["minimumFractionDigits"] = minimum_fraction_digits
        if maximum_fraction_digits is not None:
            number_config["maximumFractionDigits"] = maximum_fraction_digits
        self._render_config.update(number_config)
        return self
    
    def date_format(
        self,
        format_string: str = "YYYY-MM-DD HH:mm:ss"
    ) -> "ColumnConfig":
        """
        Configure date formatting for a date column.
        
        Args:
            format_string: Date format pattern (e.g., 'YYYY-MM-DD', 'MM/DD/YYYY HH:mm')
            
        Returns:
            self for method chaining
        """
        self._config["render"] = self.RENDER_DATE
        self._render_config["dateFormat"] = format_string
        return self
    
    def boolean_format(
        self,
        true_text: str = "Yes",
        false_text: str = "No"
    ) -> "ColumnConfig":
        """
        Configure display text for boolean values.
        
        Args:
            true_text: Text to display for true values
            false_text: Text to display for false values
            
        Returns:
            self for method chaining
        """
        self._config["render"] = self.RENDER_BOOLEAN
        self._render_config["trueText"] = true_text
        self._render_config["falseText"] = false_text
        return self
    
    def progress_bar(
        self,
        min_value: float = 0,
        max_value: float = 100,
        show_value: bool = True
    ) -> "ColumnConfig":
        """
        Configure a progress bar render for the column.
        
        Args:
            min_value: Minimum value for the progress bar
            max_value: Maximum value for the progress bar
            show_value: Whether to display the value text
            
        Returns:
            self for method chaining
        """
        self._config["render"] = self.RENDER_PROGRESS
        self._render_config["min"] = min_value
        self._render_config["max"] = max_value
        self._render_config["showValue"] = show_value
        return self
    
    def embedded_view(
        self,
        path: str,
        params: Optional[Dict[str, Any]] = None
    ) -> "ColumnConfig":
        """
        Configure an embedded view render for the column.
        
        Args:
            path: Path to the Perspective view to embed
            params: Parameters to pass to the embedded view
            
        Returns:
            self for method chaining
        """
        self._config["render"] = self.RENDER_VIEW
        self._render_config["viewPath"] = path
        if params:
            self._render_config["viewParams"] = params
        return self
    
    def style(
        self,
        background_color: Optional[str] = None,
        color: Optional[str] = None,
        font_weight: Optional[str] = None,
        font_style: Optional[str] = None,
        **custom_styles: Any
    ) -> "ColumnConfig":
        """
        Configure styling for the column.
        
        Args:
            background_color: Background color for cells
            color: Text color for cells
            font_weight: Font weight (e.g., 'bold')
            font_style: Font style (e.g., 'italic')
            **custom_styles: Additional CSS style properties
            
        Returns:
            self for method chaining
        """
        if background_color is not None:
            self._style["backgroundColor"] = background_color
        if color is not None:
            self._style["color"] = color
        if font_weight is not None:
            self._style["fontWeight"] = font_weight
        if font_style is not None:
            self._style["fontStyle"] = font_style
        self._style.update(custom_styles)
        return self
    
    def filter(
        self,
        enabled: bool = True,
        filter_type: Optional[str] = None
    ) -> "ColumnConfig":
        """
        Configure filtering for the column.
        
        Args:
            enabled: Whether filtering is enabled
            filter_type: Type of filter to use
            
        Returns:
            self for method chaining
        """
        self._filter_config["enabled"] = enabled
        if filter_type is not None:
            self._filter_config["type"] = filter_type
        return self
    
    def strict_width(self, width: int) -> "ColumnConfig":
        """
        Set a strict fixed width for the column.
        
        Args:
            width: Width in pixels
            
        Returns:
            self for method chaining
        """
        self._config["width"] = width
        self._config["minWidth"] = width
        self._config["maxWidth"] = width
        return self
    
    def build(self) -> Dict[str, Any]:
        """
        Build and return the final column configuration dictionary.
        
        Returns:
            Dictionary representing the column configuration
        """
        config = dict(self._config)
        config["header"] = dict(self._header)
        
        if self._render_config:
            if "renderConfig" not in config:
                config["renderConfig"] = {}
            config["renderConfig"].update(self._render_config)
            
        if self._style:
            config["style"] = dict(self._style)
            
        if self._filter_config:
            config["filter"] = dict(self._filter_config)
            
        return config


class ColumnBuilder:
    """
    Factory class for creating common column configurations.
    
    Provides static methods for quickly creating columns with
    common configurations for different data types.
    """
    
    @staticmethod
    def text(
        field: str,
        title: Optional[str] = None,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a text column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).render(ColumnConfig.RENDER_STRING)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def number(
        field: str,
        title: Optional[str] = None,
        decimals: int = 2,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a number column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            decimals: Number of decimal places
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).number_format(
            minimum_fraction_digits=decimals,
            maximum_fraction_digits=decimals
        ).justify(ColumnConfig.JUSTIFY_RIGHT)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def currency(
        field: str,
        title: Optional[str] = None,
        symbol: str = "$",
        decimals: int = 2,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a currency column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            symbol: Currency symbol
            decimals: Number of decimal places
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        format_str = f"{symbol}0,0.{'0' * decimals}"
        config = ColumnConfig(field).number_format(
            format_string=format_str
        ).justify(ColumnConfig.JUSTIFY_RIGHT)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def date(
        field: str,
        title: Optional[str] = None,
        format_string: str = "YYYY-MM-DD",
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a date column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            format_string: Date format pattern
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).date_format(format_string)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def datetime(
        field: str,
        title: Optional[str] = None,
        format_string: str = "YYYY-MM-DD HH:mm:ss",
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a datetime column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            format_string: DateTime format pattern
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).date_format(format_string)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def boolean(
        field: str,
        title: Optional[str] = None,
        true_text: str = "Yes",
        false_text: str = "No",
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a boolean column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            true_text: Text to display for true values
            false_text: Text to display for false values
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).boolean_format(true_text, false_text)
        config.justify(ColumnConfig.JUSTIFY_CENTER)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def toggle(
        field: str,
        title: Optional[str] = None,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a toggle/checkbox column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).render(ColumnConfig.RENDER_TOGGLE)
        config.justify(ColumnConfig.JUSTIFY_CENTER)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def progress(
        field: str,
        title: Optional[str] = None,
        min_value: float = 0,
        max_value: float = 100,
        show_value: bool = True,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create a progress bar column configuration.
        
        Args:
            field: Field name in the data source
            title: Display title (defaults to field name)
            min_value: Minimum value
            max_value: Maximum value
            show_value: Whether to show value text
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).progress_bar(min_value, max_value, show_value)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def view(
        field: str,
        view_path: str,
        title: Optional[str] = None,
        params: Optional[Dict[str, Any]] = None,
        width: Optional[int] = None
    ) -> ColumnConfig:
        """
        Create an embedded view column configuration.
        
        Args:
            field: Field name in the data source
            view_path: Path to the Perspective view
            title: Display title (defaults to field name)
            params: Parameters for the embedded view
            width: Column width in pixels
            
        Returns:
            ColumnConfig instance
        """
        config = ColumnConfig(field).embedded_view(view_path, params)
        if title:
            config.header(title=title)
        if width:
            config.width(value=width)
        return config
    
    @staticmethod
    def id_column(
        field: str = "id",
        title: str = "ID",
        width: int = 60
    ) -> ColumnConfig:
        """
        Create a standard ID column configuration.
        
        Args:
            field: Field name (default: 'id')
            title: Display title (default: 'ID')
            width: Column width (default: 60)
            
        Returns:
            ColumnConfig instance
        """
        return (ColumnConfig(field)
                .header(title=title)
                .strict_width(width)
                .justify(ColumnConfig.JUSTIFY_CENTER)
                .sortable(True)
                .editable(False)
                .resizable(False))
    
    @staticmethod
    def actions_column(
        view_path: str,
        field: str = "actions",
        title: str = "Actions",
        width: int = 120,
        params: Optional[Dict[str, Any]] = None
    ) -> ColumnConfig:
        """
        Create an actions column with an embedded view.
        
        Args:
            view_path: Path to the actions view
            field: Field name (default: 'actions')
            title: Display title (default: 'Actions')
            width: Column width (default: 120)
            params: Parameters for the view
            
        Returns:
            ColumnConfig instance
        """
        return (ColumnConfig(field)
                .header(title=title)
                .embedded_view(view_path, params)
                .strict_width(width)
                .sortable(False)
                .editable(False)
                .resizable(False))
