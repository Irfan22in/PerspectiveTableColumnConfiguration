"""
Unit Tests for Perspective Table Column Configuration

Tests for the column_builder and table_columns modules.
"""

import unittest
import json
import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from perspective_table_config import ColumnBuilder, ColumnConfig, TableColumnsBuilder
from perspective_table_config.table_columns import (
    build_columns_from_data,
    build_columns_from_fields
)


class TestColumnConfig(unittest.TestCase):
    """Tests for the ColumnConfig class."""
    
    def test_basic_column_creation(self):
        """Test basic column creation with field name."""
        config = ColumnConfig("test_field").build()
        
        self.assertEqual(config["field"], "test_field")
        self.assertTrue(config["visible"])
        self.assertEqual(config["header"]["title"], "test_field")
    
    def test_header_configuration(self):
        """Test header configuration."""
        config = (ColumnConfig("field")
                  .header(title="Custom Title", tooltip="Help text", align="center")
                  .build())
        
        self.assertEqual(config["header"]["title"], "Custom Title")
        self.assertEqual(config["header"]["tooltip"], "Help text")
        self.assertEqual(config["header"]["align"], "center")
    
    def test_width_configuration(self):
        """Test width configuration options."""
        config = (ColumnConfig("field")
                  .width(value=100, min_width=50, max_width=200, grow=1)
                  .build())
        
        self.assertEqual(config["width"], 100)
        self.assertEqual(config["minWidth"], 50)
        self.assertEqual(config["maxWidth"], 200)
        self.assertEqual(config["grow"], 1)
    
    def test_strict_width(self):
        """Test strict width sets all width properties."""
        config = ColumnConfig("field").strict_width(80).build()
        
        self.assertEqual(config["width"], 80)
        self.assertEqual(config["minWidth"], 80)
        self.assertEqual(config["maxWidth"], 80)
    
    def test_justify_options(self):
        """Test justify configuration."""
        config = ColumnConfig("field").justify("center").build()
        self.assertEqual(config["justify"], "center")
        
        config = ColumnConfig("field").justify("right").build()
        self.assertEqual(config["justify"], "right")
    
    def test_visibility(self):
        """Test visibility configuration."""
        config = ColumnConfig("field").visible(False).build()
        self.assertFalse(config["visible"])
        
        config = ColumnConfig("field").visible(True).build()
        self.assertTrue(config["visible"])
    
    def test_editable_sortable_resizable(self):
        """Test editable, sortable, and resizable configurations."""
        config = (ColumnConfig("field")
                  .editable(True)
                  .sortable(True)
                  .resizable(False)
                  .build())
        
        self.assertTrue(config["editable"])
        self.assertTrue(config["sortable"])
        self.assertFalse(config["resizable"])
    
    def test_number_format(self):
        """Test number formatting configuration."""
        config = (ColumnConfig("price")
                  .number_format(
                      format_string="$0,0.00",
                      use_grouping=True,
                      minimum_fraction_digits=2,
                      maximum_fraction_digits=2
                  )
                  .build())
        
        self.assertEqual(config["render"], "number")
        self.assertEqual(config["renderConfig"]["format"], "$0,0.00")
        self.assertTrue(config["renderConfig"]["useGrouping"])
        self.assertEqual(config["renderConfig"]["minimumFractionDigits"], 2)
        self.assertEqual(config["renderConfig"]["maximumFractionDigits"], 2)
    
    def test_date_format(self):
        """Test date formatting configuration."""
        config = ColumnConfig("date").date_format("MM/DD/YYYY").build()
        
        self.assertEqual(config["render"], "date")
        self.assertEqual(config["renderConfig"]["dateFormat"], "MM/DD/YYYY")
    
    def test_boolean_format(self):
        """Test boolean formatting configuration."""
        config = (ColumnConfig("active")
                  .boolean_format(true_text="Active", false_text="Inactive")
                  .build())
        
        self.assertEqual(config["render"], "boolean")
        self.assertEqual(config["renderConfig"]["trueText"], "Active")
        self.assertEqual(config["renderConfig"]["falseText"], "Inactive")
    
    def test_progress_bar(self):
        """Test progress bar configuration."""
        config = (ColumnConfig("progress")
                  .progress_bar(min_value=0, max_value=100, show_value=True)
                  .build())
        
        self.assertEqual(config["render"], "progress")
        self.assertEqual(config["renderConfig"]["min"], 0)
        self.assertEqual(config["renderConfig"]["max"], 100)
        self.assertTrue(config["renderConfig"]["showValue"])
    
    def test_embedded_view(self):
        """Test embedded view configuration."""
        params = {"color": "blue", "size": "small"}
        config = (ColumnConfig("custom")
                  .embedded_view(path="Views/Component", params=params)
                  .build())
        
        self.assertEqual(config["render"], "view")
        self.assertEqual(config["renderConfig"]["viewPath"], "Views/Component")
        self.assertEqual(config["renderConfig"]["viewParams"], params)
    
    def test_style_configuration(self):
        """Test style configuration."""
        config = (ColumnConfig("field")
                  .style(
                      background_color="#ffffff",
                      color="#000000",
                      font_weight="bold",
                      font_style="italic",
                      padding="10px"
                  )
                  .build())
        
        self.assertEqual(config["style"]["backgroundColor"], "#ffffff")
        self.assertEqual(config["style"]["color"], "#000000")
        self.assertEqual(config["style"]["fontWeight"], "bold")
        self.assertEqual(config["style"]["fontStyle"], "italic")
        self.assertEqual(config["style"]["padding"], "10px")
    
    def test_filter_configuration(self):
        """Test filter configuration."""
        config = (ColumnConfig("field")
                  .filter(enabled=True, filter_type="text")
                  .build())
        
        self.assertTrue(config["filter"]["enabled"])
        self.assertEqual(config["filter"]["type"], "text")
    
    def test_method_chaining(self):
        """Test that all methods return self for chaining."""
        config = (ColumnConfig("field")
                  .header(title="Title")
                  .width(value=100)
                  .justify("center")
                  .visible(True)
                  .editable(True)
                  .sortable(True)
                  .resizable(True)
                  .render("string")
                  .style(color="red")
                  .filter(enabled=True)
                  .build())
        
        self.assertIsInstance(config, dict)
        self.assertEqual(config["field"], "field")


class TestColumnBuilder(unittest.TestCase):
    """Tests for the ColumnBuilder factory class."""
    
    def test_text_column(self):
        """Test text column creation."""
        config = ColumnBuilder.text("name", "Full Name", 200).build()
        
        self.assertEqual(config["field"], "name")
        self.assertEqual(config["header"]["title"], "Full Name")
        self.assertEqual(config["width"], 200)
        self.assertEqual(config["render"], "string")
    
    def test_number_column(self):
        """Test number column creation."""
        config = ColumnBuilder.number("quantity", "Qty", decimals=0, width=80).build()
        
        self.assertEqual(config["field"], "quantity")
        self.assertEqual(config["render"], "number")
        self.assertEqual(config["justify"], "right")
        self.assertEqual(config["renderConfig"]["minimumFractionDigits"], 0)
    
    def test_currency_column(self):
        """Test currency column creation."""
        config = ColumnBuilder.currency("price", "Price", "$", 2, 100).build()
        
        self.assertEqual(config["field"], "price")
        self.assertEqual(config["render"], "number")
        self.assertIn("$", config["renderConfig"]["format"])
    
    def test_date_column(self):
        """Test date column creation."""
        config = ColumnBuilder.date("birth_date", "Birthday", "MM/DD/YYYY", 120).build()
        
        self.assertEqual(config["field"], "birth_date")
        self.assertEqual(config["render"], "date")
        self.assertEqual(config["renderConfig"]["dateFormat"], "MM/DD/YYYY")
    
    def test_datetime_column(self):
        """Test datetime column creation."""
        config = ColumnBuilder.datetime("timestamp", "Timestamp").build()
        
        self.assertEqual(config["field"], "timestamp")
        self.assertEqual(config["render"], "date")
        self.assertIn("HH:mm:ss", config["renderConfig"]["dateFormat"])
    
    def test_boolean_column(self):
        """Test boolean column creation."""
        config = ColumnBuilder.boolean("active", "Status", "On", "Off", 80).build()
        
        self.assertEqual(config["field"], "active")
        self.assertEqual(config["render"], "boolean")
        self.assertEqual(config["justify"], "center")
        self.assertEqual(config["renderConfig"]["trueText"], "On")
    
    def test_toggle_column(self):
        """Test toggle column creation."""
        config = ColumnBuilder.toggle("enabled", "Enable", 60).build()
        
        self.assertEqual(config["field"], "enabled")
        self.assertEqual(config["render"], "toggle")
        self.assertEqual(config["justify"], "center")
    
    def test_progress_column(self):
        """Test progress column creation."""
        config = ColumnBuilder.progress("completion", "Progress", 0, 100, True, 150).build()
        
        self.assertEqual(config["field"], "completion")
        self.assertEqual(config["render"], "progress")
    
    def test_view_column(self):
        """Test embedded view column creation."""
        config = ColumnBuilder.view(
            "custom", "Views/Custom", "Custom", {"param": "value"}, 120
        ).build()
        
        self.assertEqual(config["field"], "custom")
        self.assertEqual(config["render"], "view")
        self.assertEqual(config["renderConfig"]["viewPath"], "Views/Custom")
    
    def test_id_column(self):
        """Test ID column creation."""
        config = ColumnBuilder.id_column("user_id", "User ID", 80).build()
        
        self.assertEqual(config["field"], "user_id")
        self.assertEqual(config["header"]["title"], "User ID")
        self.assertEqual(config["width"], 80)
        self.assertEqual(config["minWidth"], 80)
        self.assertEqual(config["maxWidth"], 80)
        self.assertTrue(config["sortable"])
        self.assertFalse(config["editable"])
    
    def test_actions_column(self):
        """Test actions column creation."""
        config = ColumnBuilder.actions_column(
            "Views/Actions", "action_col", "Actions", 150
        ).build()
        
        self.assertEqual(config["field"], "action_col")
        self.assertEqual(config["render"], "view")
        self.assertFalse(config["sortable"])
        self.assertFalse(config["editable"])


class TestTableColumnsBuilder(unittest.TestCase):
    """Tests for the TableColumnsBuilder class."""
    
    def test_basic_initialization(self):
        """Test basic builder initialization."""
        builder = TableColumnsBuilder()
        self.assertEqual(builder.build(), [])
    
    def test_add_column(self):
        """Test adding a column directly."""
        builder = TableColumnsBuilder()
        builder.add_column(ColumnConfig("test"))
        
        columns = builder.build()
        self.assertEqual(len(columns), 1)
        self.assertEqual(columns[0]["field"], "test")
    
    def test_from_field_list(self):
        """Test generating columns from field list."""
        builder = TableColumnsBuilder()
        columns = builder.from_field_list(["id", "name", "email"]).build()
        
        self.assertEqual(len(columns), 3)
        fields = [c["field"] for c in columns]
        self.assertIn("id", fields)
        self.assertIn("name", fields)
        self.assertIn("email", fields)
    
    def test_from_data(self):
        """Test generating columns from data."""
        data = [{"id": 1, "name": "Test", "value": 100}]
        
        builder = TableColumnsBuilder()
        columns = builder.from_data(data).build()
        
        self.assertEqual(len(columns), 3)
        fields = [c["field"] for c in columns]
        self.assertIn("id", fields)
        self.assertIn("name", fields)
        self.assertIn("value", fields)
    
    def test_from_data_single_dict(self):
        """Test generating columns from single dict."""
        data = {"id": 1, "name": "Test"}
        
        builder = TableColumnsBuilder()
        columns = builder.from_data(data).build()
        
        self.assertEqual(len(columns), 2)
    
    def test_from_empty_data(self):
        """Test handling empty data."""
        builder = TableColumnsBuilder()
        columns = builder.from_data([]).build()
        self.assertEqual(columns, [])
    
    def test_exclude_fields(self):
        """Test excluding fields."""
        builder = TableColumnsBuilder()
        builder.exclude_fields("internal", "_hidden")
        
        columns = builder.from_field_list(
            ["id", "name", "internal", "_hidden"]
        ).build()
        
        fields = [c["field"] for c in columns]
        self.assertEqual(len(columns), 2)
        self.assertNotIn("internal", fields)
        self.assertNotIn("_hidden", fields)
    
    def test_field_overrides(self):
        """Test field overrides."""
        custom_config = ColumnConfig("status").header(title="Custom Status")
        
        builder = TableColumnsBuilder()
        builder.add_field_override("status", custom_config)
        
        columns = builder.from_field_list(["id", "status"]).build()
        
        status_col = next(c for c in columns if c["field"] == "status")
        self.assertEqual(status_col["header"]["title"], "Custom Status")
    
    def test_default_settings(self):
        """Test default settings."""
        builder = TableColumnsBuilder()
        builder.set_default_settings(sortable=True, editable=False, width=100)
        
        columns = builder.from_field_list(["field1", "field2"]).build()
        
        for col in columns:
            self.assertTrue(col["sortable"])
            self.assertFalse(col["editable"])
            self.assertEqual(col["width"], 100)
    
    def test_custom_type_rules(self):
        """Test custom type rules."""
        builder = TableColumnsBuilder()
        builder.add_type_rule(
            "code",
            lambda f, t: ColumnBuilder.text(f, t).style(font_weight="bold")
        )
        
        columns = builder.from_field_list(["product_code"]).build()
        
        self.assertEqual(columns[0]["style"]["fontWeight"], "bold")
    
    def test_type_detection_date(self):
        """Test automatic date type detection."""
        builder = TableColumnsBuilder()
        columns = builder.from_field_list(["created_date", "updated_at"]).build()
        
        for col in columns:
            self.assertEqual(col["render"], "date")
    
    def test_type_detection_boolean(self):
        """Test automatic boolean type detection."""
        builder = TableColumnsBuilder()
        columns = builder.from_field_list(["is_active", "has_permission"]).build()
        
        for col in columns:
            self.assertEqual(col["render"], "boolean")
    
    def test_type_detection_currency(self):
        """Test automatic currency type detection."""
        builder = TableColumnsBuilder()
        columns = builder.from_field_list(["price", "total_cost"]).build()
        
        for col in columns:
            self.assertEqual(col["render"], "number")
    
    def test_reorder(self):
        """Test column reordering."""
        builder = TableColumnsBuilder()
        builder.from_field_list(["name", "id", "status"])
        builder.reorder("id", "name")
        
        columns = builder.build()
        self.assertEqual(columns[0]["field"], "id")
        self.assertEqual(columns[1]["field"], "name")
        self.assertEqual(columns[2]["field"], "status")
    
    def test_clear(self):
        """Test clearing columns."""
        builder = TableColumnsBuilder()
        builder.from_field_list(["field1", "field2"])
        builder.clear()
        
        self.assertEqual(builder.build(), [])
    
    def test_build_json(self):
        """Test JSON output."""
        builder = TableColumnsBuilder()
        builder.add_column(ColumnConfig("test"))
        
        json_output = builder.build_json()
        parsed = json.loads(json_output)
        
        self.assertEqual(len(parsed), 1)
        self.assertEqual(parsed[0]["field"], "test")
    
    def test_humanize_field_name(self):
        """Test field name humanization."""
        builder = TableColumnsBuilder()
        
        # Test camelCase
        self.assertEqual(builder._humanize_field_name("firstName"), "First Name")
        
        # Test snake_case
        self.assertEqual(builder._humanize_field_name("first_name"), "First Name")
        
        # Test kebab-case
        self.assertEqual(builder._humanize_field_name("first-name"), "First Name")


class TestConvenienceFunctions(unittest.TestCase):
    """Tests for convenience functions."""
    
    def test_build_columns_from_data(self):
        """Test build_columns_from_data function."""
        data = [{"id": 1, "name": "Test", "internal": "hidden"}]
        
        columns = build_columns_from_data(
            data,
            exclude_fields=["internal"],
            sortable=True,
            editable=False
        )
        
        self.assertEqual(len(columns), 2)
        fields = [c["field"] for c in columns]
        self.assertNotIn("internal", fields)
    
    def test_build_columns_from_fields(self):
        """Test build_columns_from_fields function."""
        fields = ["id", "name", "status"]
        
        columns = build_columns_from_fields(
            fields,
            sortable=False,
            editable=True
        )
        
        self.assertEqual(len(columns), 3)
        for col in columns:
            self.assertFalse(col["sortable"])
            self.assertTrue(col["editable"])
    
    def test_build_with_overrides(self):
        """Test building with field overrides."""
        custom_status = ColumnConfig("status").embedded_view("Views/Status")
        
        columns = build_columns_from_fields(
            ["id", "name", "status"],
            field_overrides={"status": custom_status}
        )
        
        status_col = next(c for c in columns if c["field"] == "status")
        self.assertEqual(status_col["render"], "view")


class TestEdgeCases(unittest.TestCase):
    """Tests for edge cases and error handling."""
    
    def test_empty_field_name(self):
        """Test handling empty field name."""
        config = ColumnConfig("").build()
        self.assertEqual(config["field"], "")
    
    def test_special_characters_in_field(self):
        """Test handling special characters in field names."""
        config = ColumnConfig("field.with.dots").build()
        self.assertEqual(config["field"], "field.with.dots")
    
    def test_unicode_field_name(self):
        """Test handling unicode in field names."""
        config = ColumnConfig("フィールド").build()
        self.assertEqual(config["field"], "フィールド")
    
    def test_none_values_in_optional_params(self):
        """Test that None values don't affect config."""
        config = (ColumnConfig("field")
                  .header(title=None, tooltip=None)
                  .width(value=None, min_width=None)
                  .build())
        
        self.assertNotIn("tooltip", config["header"])
        self.assertNotIn("width", config)
    
    def test_multiple_render_calls(self):
        """Test that multiple render calls override correctly."""
        config = (ColumnConfig("field")
                  .render("string")
                  .render("number")
                  .build())
        
        self.assertEqual(config["render"], "number")
    
    def test_builder_reuse(self):
        """Test that builder can be reused after build."""
        builder = TableColumnsBuilder()
        builder.from_field_list(["field1"])
        
        first_build = builder.build()
        
        builder.add_column(ColumnConfig("field2"))
        second_build = builder.build()
        
        self.assertEqual(len(first_build), 1)
        self.assertEqual(len(second_build), 2)


if __name__ == "__main__":
    unittest.main()
