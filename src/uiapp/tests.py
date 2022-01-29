import xml

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

x = """
<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><hierarchy rotation="0"><node index="0" text="" resource-id="" class="android.widget.FrameLayout" package="com.example.hccr_sdk_10" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,0][1200,1920]"><node index="0" text="hccr_sdk_1.0" resource-id="" class="android.widget.TextView" package="com.example.hccr_sdk_10" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[48,85][296,139]" /><node index="1" text="HCCR  SDK" resource-id="" class="android.widget.TextView" package="com.example.hccr_sdk_10" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,176][1200,276]" /><node index="2" text="" resource-id="com.example.hccr_sdk_10:id/origin_image" class="android.widget.ImageView" package="com.example.hccr_sdk_10" content-desc="image" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,276][1200,976]" /><node index="3" text="手写识别" resource-id="com.example.hccr_sdk_10:id/inference" class="android.widget.Button" package="com.example.hccr_sdk_10" content-desc="" checkable="false" checked="false" clickable="true" enabled="true" focusable="true" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,976][1200,1076]" /><node index="4" text="" resource-id="com.example.hccr_sdk_10:id/show_result" class="android.widget.TextView" package="com.example.hccr_sdk_10" content-desc="" checkable="false" checked="false" clickable="false" enabled="true" focusable="false" focused="false" scrollable="false" long-clickable="false" password="false" selected="false" bounds="[0,1076][1200,1776]" /></node></hierarchy>
"""

# xml.s.parseString(xmlstring, contenthandler[, errorhandler])
# tree = ET.ElementTree(element=x)
# treeIter = tree.iter(tag="node")

