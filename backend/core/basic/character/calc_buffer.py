from core.basic.property import CharacterInfo
from ..roleinfo import get_key_by_value
from .base import CharacterBase


class CalcBufferMixin(CharacterBase):
    """辅助角色 Buff 技能计算相关方法"""

    # region 辅助计算项

    def calc_buffer_skills(self):
        skillInfos = []
        # 适用属性
        main = getattr(self, get_key_by_value(self.适用属性))
        # 增益量
        buffer_power = self.Buffer * self.BufferP
        # buff系数
        buff_ratio_new = (main / 2993 + 1) * (buffer_power / 4800 + 1) if buffer_power > 0 else 0
        buff_ratio_old = main / 2993 + 1
        # 觉醒系数
        awake_ratio_new = ((main + 7500) / 7500 + 1) * ((buffer_power + 68000) / 8500 + 1) if buffer_power > 0 else 0
        awake_ratio_old = main / 7500 + 1
        for i in self.skills:
            if i.lv > 0 and i.hasUP and i.up is not None and i.up > 0:
                self.SetStatus(四维=40)
            if i.buffer and i.lv > 0:
                info = i.skillInfo()
                value = info[0]
                if i.buffType == 'buff' or i.buffType == 'buffSub':
                    value1 = (info[1][0] + info[1][2]) * info[1][1] * buff_ratio_old + info[1][0] * buff_ratio_new
                    value2 = (info[2][0] + info[2][2]) * info[2][1] * buff_ratio_old + info[2][0] * buff_ratio_new
                elif i.buffType == 'awake' or i.buffType == 'awakeSub':
                    value1 = (info[1][0] + info[1][2]) * info[1][1] * awake_ratio_old + info[1][0] * awake_ratio_new
                    value2 = (info[2][0] + info[2][2]) * info[2][1] * awake_ratio_old + info[2][0] * awake_ratio_new
                else:
                    value1 = (info[1][0] + info[1][2]) * info[1][1]
                    value2 = (info[2][0] + info[2][2]) * info[2][1]
                value3 = info[3]
                value4 = info[4]
                if i.buffType == 'awake' and self.bindAwake == 50:
                    pass
                else:
                    skillInfos.append(
                        {
                            'name': i.name,
                            'cd': value4,
                            'icon': i.icon,
                            'lv': i.lv,
                            'buff': [value, value1, value2, value3],
                            'type': i.type,
                        }
                    )
        return skillInfos

    def get_buffer_info(self):
        attrs = [get_key_by_value(self.适用属性), 'Buffer', 'BufferP']
        info = []
        for attr in attrs:
            temp = getattr(CharacterInfo, attr)
            value = getattr(self, attr)
            info.append({'name': temp.name, 'value': temp.value(value)})
        return info

    # endregion
