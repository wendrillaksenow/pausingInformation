import globalPluginHandler
import controlTypes
import ui
import addonHandler
import gettext

# Inicializa o sistema de internacionalização
addonHandler.initTranslation()

# Mapeamento manual de tipos de controle e estados para nomes correspondentes em inglês
CONTROL_TYPE_NAMES = {
    controlTypes.ROLE_CHECKBOX: _("check box"),
    controlTypes.ROLE_RADIOBUTTON: _("radio button"),
    controlTypes.ROLE_MENUBUTTON: _("menu button"),
    controlTypes.ROLE_EDITABLETEXT: _("editable text"),
    controlTypes.ROLE_LISTITEM: _("list item"),
    controlTypes.ROLE_MENUITEM: _("menu item"),
    controlTypes.ROLE_ICON: _("icon"),
}

STATE_NAMES = {
    controlTypes.STATE_UNAVAILABLE: _("unavailable"),
    controlTypes.STATE_BUSY: _("busy"),
}

class GlobalPlugin(globalPluginHandler.GlobalPlugin):
    def __init__(self):
        super(GlobalPlugin, self).__init__()

    def event_gainFocus(self, obj, nextHandler):
        try:
            # Lê o texto selecionado quando o objeto em foco é uma caixa de edição
            if obj.role == controlTypes.ROLE_EDITABLETEXT:
                selection = obj.getTextWithFields(obj.selectionStart, obj.selectionEnd)
                if selection:
                    ui.message(_("Selected text: {text}").format(text=selection))

            # Obtenha a descrição padrão do objeto
            description = obj.name if obj.name else ""
            additional_info = []

            # Adiciona o papel do objeto (roleText)
            control_type = controlTypes.roleLabels.get(obj.role, _("unknown control type"))
            additional_info.append(control_type)

            # Adiciona os estados do objeto (states) convertendo-os para strings legíveis
            if obj.states:
                state_descriptions = []
                for state in obj.states:
                    # Exclui "focused" e "selected"
                    if state not in [controlTypes.STATE_FOCUSED, controlTypes.STATE_SELECTED]:
                        state_name = controlTypes.stateLabels.get(state, _("unknown state"))
                        state_descriptions.append(state_name)
                if state_descriptions:
                    additional_info.extend(state_descriptions)
                else:
                    additional_info.append(_("unknown state"))
            else:
                additional_info.append(_("unknown state"))

            # Adiciona a descrição do objeto (description)
            if obj.description:
                additional_info.append(str(obj.description))

            # Constrói a string com pausas
            final_description = description
            if additional_info:
                if final_description:
                    final_description += " - " + " - ".join(additional_info)
                else:
                    final_description = " - ".join(additional_info)

            # Verifica se o objeto é um item de lista ou menu e ajusta a descrição
            if obj.role == controlTypes.ROLE_LISTITEM:
                if obj.indexInParent is not None and obj.parent.childCount is not None:
                    final_description += f" - {obj.indexInParent + 1} de {obj.parent.childCount}"
            elif obj.role == controlTypes.ROLE_MENUITEM:
                if obj.name and obj.shortcut:
                    final_description += f" - {obj.name} {obj.shortcut}"
            elif obj.role == controlTypes.ROLE_ICON:
                if obj.indexInParent is not None and obj.parent.childCount is not None:
                    final_description += f" - ícone {obj.indexInParent + 1} de {obj.parent.childCount}"

            # Lê a descrição modificada
            if final_description:
                ui.message(final_description)
            else:
                nextHandler()
        except Exception as e:
            nextHandler()
