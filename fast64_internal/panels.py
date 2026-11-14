import bpy


class Fast64MaterialPanel(bpy.types.Panel):
    bl_label = "Fast64"
    bl_idname = "MATERIAL_PT_fast64"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "material"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 100

    @classmethod
    def poll(cls, context):
        return context.object is not None and hasattr(context.object.data, "materials")

    def draw(self, context):
        pass


class Fast64ObjectPanel(bpy.types.Panel):
    bl_label = "Fast64"
    bl_idname = "OBJECT_PT_fast64"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 100

    @classmethod
    def poll(cls, context):
        return context.object is not None

    def draw(self, context):
        pass


class Fast64WorldPanel(bpy.types.Panel):
    bl_label = "Fast64"
    bl_idname = "WORLD_PT_fast64"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "world"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 100

    @classmethod
    def poll(cls, context):
        return context.world is not None

    def draw(self, context):
        pass


class Fast64BonePanel(bpy.types.Panel):
    bl_label = "Fast64"
    bl_idname = "BONE_PT_fast64"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "bone"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 100

    @classmethod
    def poll(cls, context):
        return context.bone is not None

    def draw(self, context):
        pass


class Fast64CameraPanel(bpy.types.Panel):
    bl_label = "Fast64"
    bl_idname = "DATA_PT_fast64_camera"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "data"
    bl_options = {"DEFAULT_CLOSED"}
    bl_order = 100

    @classmethod
    def poll(cls, context):
        from .sm64.sm64_camera import CameraSettingsPanel

        return context.camera is not None and CameraSettingsPanel.is_registered

    def draw(self, context):
        pass


properties_panel_classes = (
    Fast64MaterialPanel,
    Fast64ObjectPanel,
    Fast64WorldPanel,
    Fast64BonePanel,
    Fast64CameraPanel,
)


def properties_panels_register():
    for cls in properties_panel_classes:
        bpy.utils.register_class(cls)


def properties_panels_unregister():
    for cls in reversed(properties_panel_classes):
        bpy.utils.unregister_class(cls)


class SM64_Panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "SM64"
    bl_options = {"DEFAULT_CLOSED"}

    # If bl_context is 'object' and object_type is defined, only show if the object is in the types
    bl_context = ""
    object_type: list | None = None

    # goal refers to the selected enum_sm64_goal_type in SM64_Properties,
    # a different selection than this goal will filter this panel out
    goal = "All"
    # if this is True, the panel is hidden whenever the scene's export_type is not 'C'
    decomp_only = False
    # if this is True, the panel is hidden whenever the scene's export_type is 'C'
    binary_only = False
    import_panel = False

    @classmethod
    def poll(cls, context):
        if cls.bl_context == "object":
            if cls.object_type and context.object.type not in cls.object_type:
                return False
        sm64_props = context.scene.fast64.sm64
        if context.scene.gameEditorMode != "SM64":
            return False
        elif cls.import_panel and not sm64_props.show_importing_menus:
            return False
        elif cls.decomp_only and sm64_props.export_type != "C":
            return False
        elif cls.binary_only and sm64_props.export_type == "C":
            return False
        scene_goal = sm64_props.goal
        return scene_goal == "All" or sm64_props.goal == cls.goal or cls.goal == "All"


class Z64_Panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "OOT/MM"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.gameEditorMode in {"OOT", "MM"}


class MK64_Panel(bpy.types.Panel):
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "MK64"
    bl_options = {"DEFAULT_CLOSED"}

    @classmethod
    def poll(cls, context):
        return context.scene.gameEditorMode == "MK64"
