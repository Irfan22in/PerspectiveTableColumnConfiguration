# -*- coding: utf-8 -*-
"""
Tests for Perspective Table Column Configuration Module

This module contains unit tests for:
    - PerspectiveColumnProps
    - SchemaColumnInformation
    - TableComponentColumnConfiguration
    - ViewRobotDetails
    - ColumnConfigurator
"""

import sys
import os
import unittest

# Add the shared_library to the path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from shared_library.perspective_column_config import (
    PerspectiveColumnProps,
    SchemaColumnInformation,
    TableComponentColumnConfiguration,
    ViewRobotDetails,
    ColumnConfigurator
)


class TestPerspectiveColumnProps(unittest.TestCase):
    """Tests for PerspectiveColumnProps class."""
    
    def test_init_default_values(self):
        """Test that default values are set correctly."""
        col = PerspectiveColumnProps()
        
        self.assertEqual(col.field, "")
        self.assertTrue(col.visible)
        self.assertFalse(col.editable)
        self.assertEqual(col.render, "auto")
        self.assertEqual(col.justify, "auto")
        self.assertEqual(col.align, "center")
        self.assertTrue(col.resizable)
        self.assertTrue(col.sortable)
        self.assertEqual(col.sort, "none")
        self.assertFalse(col.filter["enabled"])
        self.assertEqual(col.viewPath, "")
        self.assertEqual(col.viewParams, {})
        self.assertEqual(col.boolean, "checkbox")
        self.assertEqual(col.number, "value")
        self.assertEqual(col.numberFormat, "0,0.##")
        self.assertEqual(col.dateFormat, "MM/DD/YYYY")
        self.assertEqual(col.width, 200)
        self.assertFalse(col.strictWidth)
    
    def test_init_with_field(self):
        """Test initialization with a field name."""
        col = PerspectiveColumnProps(field="Robot__name")
        self.assertEqual(col.field, "Robot__name")
    
    def test_set_visible(self):
        """Test setting visibility."""
        col = PerspectiveColumnProps()
        col.set_visible(False)
        self.assertFalse(col.visible)
        
        col.set_visible(True)
        self.assertTrue(col.visible)
    
    def test_set_editable(self):
        """Test setting editability."""
        col = PerspectiveColumnProps()
        col.set_editable(True)
        self.assertTrue(col.editable)
    
    def test_set_render(self):
        """Test setting render type."""
        col = PerspectiveColumnProps()
        
        for option in PerspectiveColumnProps.RENDER_OPTIONS:
            col.set_render(option)
            self.assertEqual(col.render, option)
    
    def test_set_render_invalid(self):
        """Test that invalid render value raises error."""
        col = PerspectiveColumnProps()
        
        with self.assertRaises(ValueError):
            col.render = "invalid_render"
    
    def test_set_sortable(self):
        """Test setting sortability."""
        col = PerspectiveColumnProps()
        col.set_sortable(False)
        self.assertFalse(col.sortable)
    
    def test_set_filter_enabled(self):
        """Test setting filter enabled."""
        col = PerspectiveColumnProps()
        col.set_filter_enabled(True)
        self.assertTrue(col.filter["enabled"])
    
    def test_set_view_path(self):
        """Test setting view path."""
        col = PerspectiveColumnProps()
        col.set_view_path("/views/embedded/RobotStatus")
        self.assertEqual(col.viewPath, "/views/embedded/RobotStatus")
    
    def test_set_view_params(self):
        """Test setting view params."""
        col = PerspectiveColumnProps()
        params = {"robotId": 1, "status": "active"}
        col.set_view_params(params)
        self.assertEqual(col.viewParams, params)
    
    def test_set_view_params_invalid(self):
        """Test that invalid view params raises error."""
        col = PerspectiveColumnProps()
        
        with self.assertRaises(ValueError):
            col.viewParams = "not a dict"
    
    def test_set_null_format_value(self):
        """Test setting null format value."""
        col = PerspectiveColumnProps()
        col.set_null_format_value("N/A")
        self.assertEqual(col.nullFormat["nullFormatValue"], "N/A")
    
    def test_set_header_title(self):
        """Test setting header title."""
        col = PerspectiveColumnProps()
        col.set_header_title("Robot Name")
        self.assertEqual(col.header["title"], "Robot Name")
    
    def test_set_number_format(self):
        """Test setting number format."""
        col = PerspectiveColumnProps()
        col.set_number_format("0.00")
        self.assertEqual(col.numberFormat, "0.00")
    
    def test_set_date_format(self):
        """Test setting date format."""
        col = PerspectiveColumnProps()
        col.set_date_format("MM/DD/YYYY HH:mm:ss")
        self.assertEqual(col.dateFormat, "MM/DD/YYYY HH:mm:ss")
    
    def test_to_dict(self):
        """Test converting to dictionary."""
        col = PerspectiveColumnProps(field="Robot__name")
        col.set_visible(True)
        col.set_header_title("Robot Name")
        
        result = col.to_dict()
        
        self.assertIsInstance(result, dict)
        self.assertEqual(result["field"], "Robot__name")
        self.assertTrue(result["visible"])
        self.assertEqual(result["header"]["title"], "Robot Name")
    
    def test_method_chaining(self):
        """Test that setter methods return self for chaining."""
        col = PerspectiveColumnProps(field="Robot__status")
        
        result = (col
            .set_visible(True)
            .set_editable(False)
            .set_render("string")
            .set_sortable(True)
            .set_header_title("Status"))
        
        self.assertEqual(result, col)
        self.assertTrue(col.visible)
        self.assertFalse(col.editable)
        self.assertEqual(col.render, "string")
        self.assertTrue(col.sortable)
        self.assertEqual(col.header["title"], "Status")


class TestSchemaColumnInformation(unittest.TestCase):
    """Tests for SchemaColumnInformation class."""
    
    def test_init_with_table_column_format(self):
        """Test initialization with Table__columnName format."""
        col = SchemaColumnInformation("Robot__name")
        
        self.assertEqual(col.field, "Robot__name")
        self.assertEqual(col.table_name, "Robot")
        self.assertEqual(col.column_name, "name")
        self.assertEqual(col.ui_display_name, "name")
        self.assertEqual(col.header["title"], "name")
    
    def test_init_with_ui_display_name(self):
        """Test initialization with custom UI display name."""
        col = SchemaColumnInformation("Robot__serialNumber", ui_display_name="Serial Number")
        
        self.assertEqual(col.ui_display_name, "Serial Number")
        self.assertEqual(col.header["title"], "Serial Number")
    
    def test_init_without_table_prefix(self):
        """Test initialization without Table__ prefix."""
        col = SchemaColumnInformation("simpleColumn")
        
        self.assertEqual(col.field, "simpleColumn")
        self.assertEqual(col.table_name, "")
        self.assertEqual(col.column_name, "simpleColumn")
    
    def test_auto_render_for_integer(self):
        """Test automatic render configuration for integer type."""
        col = SchemaColumnInformation("Robot__count", data_type="integer")
        self.assertEqual(col.render, "number")
    
    def test_auto_render_for_float(self):
        """Test automatic render configuration for float type."""
        col = SchemaColumnInformation("Robot__temperature", data_type="float")
        self.assertEqual(col.render, "number")
    
    def test_auto_render_for_decimal(self):
        """Test automatic render configuration for decimal type."""
        col = SchemaColumnInformation("Robot__price", data_type="decimal(10,2)")
        self.assertEqual(col.render, "number")
    
    def test_auto_render_for_date(self):
        """Test automatic render configuration for date type."""
        col = SchemaColumnInformation("Robot__createdAt", data_type="datetime")
        self.assertEqual(col.render, "date")
    
    def test_auto_render_for_boolean(self):
        """Test automatic render configuration for boolean type."""
        col = SchemaColumnInformation("Robot__isActive", data_type="boolean")
        self.assertEqual(col.render, "boolean")
    
    def test_auto_render_for_bit(self):
        """Test automatic render configuration for bit type."""
        col = SchemaColumnInformation("Robot__enabled", data_type="bit")
        self.assertEqual(col.render, "boolean")
    
    def test_auto_render_for_string(self):
        """Test automatic render configuration for string type."""
        col = SchemaColumnInformation("Robot__name", data_type="varchar")
        self.assertEqual(col.render, "auto")
    
    def test_set_ui_display_name(self):
        """Test setting UI display name updates header."""
        col = SchemaColumnInformation("Robot__name")
        col.ui_display_name = "Robot Name"
        
        self.assertEqual(col.ui_display_name, "Robot Name")
        self.assertEqual(col.header["title"], "Robot Name")
    
    def test_inherits_from_perspective_column_props(self):
        """Test that SchemaColumnInformation inherits from PerspectiveColumnProps."""
        col = SchemaColumnInformation("Robot__name")
        
        self.assertIsInstance(col, PerspectiveColumnProps)
        self.assertTrue(hasattr(col, 'set_visible'))
        self.assertTrue(hasattr(col, 'set_editable'))
        self.assertTrue(hasattr(col, 'to_dict'))


class MockTableComponent:
    """Mock table component for testing."""
    
    def __init__(self, data):
        self.props = MockProps(data)


class MockProps:
    """Mock props object for testing."""
    
    def __init__(self, data):
        self.data = data
        self.columns = []


class TestTableComponentColumnConfiguration(unittest.TestCase):
    """Tests for TableComponentColumnConfiguration class."""
    
    def test_init_with_list_data(self):
        """Test initialization with list data directly."""
        data = [
            {"Robot__name": "Robot1", "Robot__status": "active"},
            {"Robot__name": "Robot2", "Robot__status": "inactive"}
        ]
        
        config = TableComponentColumnConfiguration(data)
        
        self.assertIn("Robot__name", config.columns)
        self.assertIn("Robot__status", config.columns)
    
    def test_init_with_mock_component(self):
        """Test initialization with mock table component."""
        data = [
            {"Robot__id": 1, "Robot__name": "Robot1"},
            {"Robot__id": 2, "Robot__name": "Robot2"}
        ]
        mock_component = MockTableComponent(data)
        
        config = TableComponentColumnConfiguration(mock_component)
        
        self.assertIn("Robot__id", config.columns)
        self.assertIn("Robot__name", config.columns)
    
    def test_init_with_empty_data(self):
        """Test initialization with empty data."""
        config = TableComponentColumnConfiguration([])
        
        self.assertEqual(len(config.columns), 0)
    
    def test_get_column(self):
        """Test getting a specific column."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        column = config.get_column("Robot__name")
        
        self.assertIsNotNone(column)
        self.assertEqual(column.field, "Robot__name")
    
    def test_get_column_not_found(self):
        """Test getting a non-existent column."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        column = config.get_column("NonExistent__column")
        
        self.assertIsNone(column)
    
    def test_set_column_visible(self):
        """Test setting column visibility."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_visible("Robot__name", False)
        
        self.assertFalse(config.get_column("Robot__name").visible)
    
    def test_set_column_editable(self):
        """Test setting column editability."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_editable("Robot__name", True)
        
        self.assertTrue(config.get_column("Robot__name").editable)
    
    def test_set_column_render(self):
        """Test setting column render type."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_render("Robot__name", "string")
        
        self.assertEqual(config.get_column("Robot__name").render, "string")
    
    def test_set_column_sortable(self):
        """Test setting column sortability."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_sortable("Robot__name", False)
        
        self.assertFalse(config.get_column("Robot__name").sortable)
    
    def test_set_column_filter_enabled(self):
        """Test setting column filter enabled."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_filter_enabled("Robot__name", True)
        
        self.assertTrue(config.get_column("Robot__name").filter["enabled"])
    
    def test_set_column_view_path(self):
        """Test setting column view path."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_view_path("Robot__name", "/views/RobotView")
        
        self.assertEqual(config.get_column("Robot__name").viewPath, "/views/RobotView")
    
    def test_set_column_view_params(self):
        """Test setting column view params."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        params = {"robotId": "{value}"}
        config.set_column_view_params("Robot__name", params)
        
        self.assertEqual(config.get_column("Robot__name").viewParams, params)
    
    def test_set_column_null_format_value(self):
        """Test setting column null format value."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_null_format_value("Robot__name", "N/A")
        
        self.assertEqual(config.get_column("Robot__name").nullFormat["nullFormatValue"], "N/A")
    
    def test_set_column_header_title(self):
        """Test setting column header title."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_header_title("Robot__name", "Robot Name")
        
        self.assertEqual(config.get_column("Robot__name").header["title"], "Robot Name")
    
    def test_set_column_number_format(self):
        """Test setting column number format."""
        data = [{"Robot__count": 100}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_number_format("Robot__count", "0.00")
        
        self.assertEqual(config.get_column("Robot__count").numberFormat, "0.00")
    
    def test_set_column_date_format(self):
        """Test setting column date format."""
        data = [{"Robot__createdAt": "2023-01-01"}]
        config = TableComponentColumnConfiguration(data)
        
        config.set_column_date_format("Robot__createdAt", "MM/DD/YYYY HH:mm:ss")
        
        self.assertEqual(config.get_column("Robot__createdAt").dateFormat, "MM/DD/YYYY HH:mm:ss")
    
    def test_build_columns(self):
        """Test building columns as list of dictionaries."""
        data = [
            {"Robot__id": 1, "Robot__name": "Robot1"},
        ]
        config = TableComponentColumnConfiguration(data)
        config.set_column_header_title("Robot__name", "Robot Name")
        
        columns = config.build_columns()
        
        self.assertIsInstance(columns, list)
        self.assertEqual(len(columns), 2)
        
        # Each column should be a dictionary
        for col in columns:
            self.assertIsInstance(col, dict)
            self.assertIn("field", col)
    
    def test_method_chaining(self):
        """Test that configuration methods return self for chaining."""
        data = [{"Robot__name": "Robot1"}]
        config = TableComponentColumnConfiguration(data)
        
        result = (config
            .set_column_visible("Robot__name", True)
            .set_column_editable("Robot__name", False)
            .set_column_sortable("Robot__name", True))
        
        self.assertEqual(result, config)


class TestViewRobotDetails(unittest.TestCase):
    """Tests for ViewRobotDetails class."""
    
    def test_init_inherits_from_table_config(self):
        """Test that ViewRobotDetails inherits from TableComponentColumnConfiguration."""
        data = [{"Robot__name": "Robot1"}]
        view = ViewRobotDetails(data)
        
        self.assertIsInstance(view, TableComponentColumnConfiguration)
    
    def test_configure_column_returns_configurator(self):
        """Test that configure_column returns a ColumnConfigurator."""
        data = [{"Robot__name": "Robot1"}]
        view = ViewRobotDetails(data)
        
        configurator = view.configure_column("Robot__name")
        
        self.assertIsInstance(configurator, ColumnConfigurator)


class TestColumnConfigurator(unittest.TestCase):
    """Tests for ColumnConfigurator class."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.data = [{"Robot__name": "Robot1"}]
        self.config = TableComponentColumnConfiguration(self.data)
    
    def test_fluent_configuration(self):
        """Test fluent API for column configuration."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        result = (configurator
            .visible(True)
            .editable(False)
            .render("string")
            .sortable(True)
            .filter_enabled(True)
            .header_title("Robot Name"))
        
        self.assertEqual(result, configurator)
        
        column = self.config.get_column("Robot__name")
        self.assertTrue(column.visible)
        self.assertFalse(column.editable)
        self.assertEqual(column.render, "string")
        self.assertTrue(column.sortable)
        self.assertTrue(column.filter["enabled"])
        self.assertEqual(column.header["title"], "Robot Name")
    
    def test_done_returns_parent_config(self):
        """Test that done() returns the parent configuration."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        result = configurator.visible(True).done()
        
        self.assertEqual(result, self.config)
    
    def test_view_path_configuration(self):
        """Test setting view path through configurator."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        configurator.view_path("/views/RobotView")
        
        column = self.config.get_column("Robot__name")
        self.assertEqual(column.viewPath, "/views/RobotView")
    
    def test_view_params_configuration(self):
        """Test setting view params through configurator."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        params = {"robotId": 1}
        configurator.view_params(params)
        
        column = self.config.get_column("Robot__name")
        self.assertEqual(column.viewParams, params)
    
    def test_null_format_value_configuration(self):
        """Test setting null format value through configurator."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        configurator.null_format_value("N/A")
        
        column = self.config.get_column("Robot__name")
        self.assertEqual(column.nullFormat["nullFormatValue"], "N/A")
    
    def test_number_format_configuration(self):
        """Test setting number format through configurator."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        configurator.number_format("0.00")
        
        column = self.config.get_column("Robot__name")
        self.assertEqual(column.numberFormat, "0.00")
    
    def test_date_format_configuration(self):
        """Test setting date format through configurator."""
        configurator = ColumnConfigurator(self.config, "Robot__name")
        
        configurator.date_format("MM/DD/YYYY HH:mm:ss")
        
        column = self.config.get_column("Robot__name")
        self.assertEqual(column.dateFormat, "MM/DD/YYYY HH:mm:ss")


class TestIntegration(unittest.TestCase):
    """Integration tests for the complete workflow."""
    
    def test_full_workflow(self):
        """Test complete workflow from data to column configuration."""
        # Simulate table data
        data = [
            {
                "Robot__id": 1,
                "Robot__name": "Robot Alpha",
                "Robot__status": "active",
                "Robot__temperature": 65.5,
                "Robot__lastUpdated": "2023-06-15 10:30:00"
            }
        ]
        
        # Create configuration
        config = TableComponentColumnConfiguration(data)
        
        # Configure columns
        (config
            .set_column_header_title("Robot__id", "ID")
            .set_column_visible("Robot__id", False)
            .set_column_header_title("Robot__name", "Robot Name")
            .set_column_editable("Robot__name", True)
            .set_column_header_title("Robot__status", "Status")
            .set_column_render("Robot__status", "string")
            .set_column_header_title("Robot__temperature", "Temperature")
            .set_column_number_format("Robot__temperature", "0.0")
            .set_column_header_title("Robot__lastUpdated", "Last Updated")
            .set_column_date_format("Robot__lastUpdated", "MM/DD/YYYY HH:mm:ss"))
        
        # Build columns
        columns = config.build_columns()
        
        # Verify
        self.assertEqual(len(columns), 5)
        
        # Find specific columns by field
        columns_by_field = {col["field"]: col for col in columns}
        
        self.assertFalse(columns_by_field["Robot__id"]["visible"])
        self.assertEqual(columns_by_field["Robot__name"]["header"]["title"], "Robot Name")
        self.assertTrue(columns_by_field["Robot__name"]["editable"])
        self.assertEqual(columns_by_field["Robot__status"]["render"], "string")
        self.assertEqual(columns_by_field["Robot__temperature"]["numberFormat"], "0.0")
        self.assertEqual(columns_by_field["Robot__lastUpdated"]["dateFormat"], "MM/DD/YYYY HH:mm:ss")
    
    def test_view_robot_details_workflow(self):
        """Test ViewRobotDetails workflow."""
        data = [
            {"Robot__id": 1, "Robot__name": "Robot1", "Robot__status": "active"}
        ]
        
        # Create view-specific configuration
        view = ViewRobotDetails(data)
        
        # Configure columns using fluent API
        (view.configure_column("Robot__id")
            .visible(False)
            .header_title("ID")
            .done())
        
        (view.configure_column("Robot__name")
            .visible(True)
            .editable(True)
            .header_title("Robot Name")
            .sortable(True)
            .filter_enabled(True)
            .done())
        
        (view.configure_column("Robot__status")
            .render("string")
            .header_title("Status")
            .null_format_value("N/A")
            .done())
        
        # Build columns
        columns = view.build_columns()
        
        self.assertEqual(len(columns), 3)
        
        columns_by_field = {col["field"]: col for col in columns}
        
        self.assertFalse(columns_by_field["Robot__id"]["visible"])
        self.assertTrue(columns_by_field["Robot__name"]["editable"])
        self.assertEqual(columns_by_field["Robot__status"]["nullFormat"]["nullFormatValue"], "N/A")


if __name__ == '__main__':
    unittest.main()
