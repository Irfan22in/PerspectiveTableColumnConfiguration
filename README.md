# PerspectiveTableColumnConfiguration
In ignition I want to have Jython backend script in shared libray to be able to create table component properties dynamically . Please read below requirements and come with tasks and good Plan.

I will want to have Class PerspectiveColumnProps that has all attributes of ignition perspective table column.
Below is column attributes copies from igntion.
Please note available option for some of the attributes as comment in same line.

Next I will want to have a Class SchemaColumnInformation
This class will have each column from the database with it meta data ,UI display name. 
Each column will inherit  Class PerspectiveColumnProps and map the meta data 

I want  Class TableComponentColumnConfiguration()
	def __init __(self , table_component)
This class will init all schema columns 
it will have argument table_component. 
It will build all column that are in table_component data in the form ColumProps and returns [{},{}]

Class ViewRobotDetails(TableComponentColumnConfiguration)
	 def __init__(self ,table_component):
		super(ViewRobotDetails ,self).__init__(table_component)


My idea is when view ( RobotDetails ) component table.props.data recieves dataset fromsome script .
At that point on cahngescript of table.props.data i will have this script that calls a class and build table columns 
if len(table.props.data) > 0 :
	table_component = self
	ViewRobotDetails(table_component) -- self here is the table component
	

table.props.data will be list of dictionary each dit represeting row[{},{}]
schemacolumn name will be Table__columnName
it is expected that table.props.data will have keys of the row as Table__columnName

I will aso want to run few methods on ColumnPropos settings.

visible ,editable ,render,sortable,filter.enabled,viewPath ,viewParams ,"nullFormatValue" ,header.title ,number.format ,date.format through some methods .
my sub view class should be able to call byu column name and set these prop as required 

	
PerspectiveColumnProps
#Ptyhon to perespect boolen representation
true = True 
false = False

{
  "field": "table_columnName",
  "visible": true,
  "editable": false,
  "render": "auto", # available_options = "auto" ,"number","date","boolean","string","view"
  "justify": "auto", # available_options = "auto" ,"left" ,"center" ,"right"
  "align": "center",	# available_options = "top" ,"center" ,"bottom"
  "resizable": true,
  "sortable": true,
  "sort": "none", # available_options = "none" ,"ascending" ,"descending"
  "filter": {
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
  },
  "viewPath": "",
  "viewParams": {},
  "boolean": "checkbox",# available_options = "value" ,"checkbox" ,"toggle"
  "number": "value",# available_options = "value" ,"progress"
  "progressBar": {
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
  },
  "toggleSwitch": {
    "color": {
      "selected": "",
      "unselected": ""
    }
  },
  "nullFormat": {
    "includeNullStrings": false,
    "strict": false,
    "nullFormatValue": "" # available_options = "blank" ,"N/A",null
  },
  "numberFormat": "0,0.##",
  "dateFormat": "MM/DD/YYYY", # available_options = "MM/DD/YYYY" , "MM/DD/YYYY HH:mm:ss",
  "width": 200,,
  "strictWidth": false,
  "style": {
    "classes": ""
  },
  "header": {
    "title": "UI Display name",
    "justify": "left", # available_options = "left" ,"center" ,"right"
    "align": "center", # available_options = "top" ,"center" ,"bottom"
    "style": {
      "classes": ""
    }
  },
  "footer": {
    "title": "",
    "justify": "left",
    "align": "center",
    "style": {
      "classes": ""
    }
  }
}
