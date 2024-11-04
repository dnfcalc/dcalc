from core.basic.character import Character

class Character(Character):

    def 技能冷却缩减(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却缩减 *= (1-x)
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc  and i.名称 not in excName:
                if i.是否主动 == 1:
                    i.CDR *= (1 - x)

    def 技能恢复加成(self, min: int, max: int, x: float, exc=[],excName=[]) -> None:
        if min == 1 and max == 100:
            self.冷却恢复 += x
        for i in self.技能栏:
            if i.所在等级 >= min and i.所在等级 <= max and i.所在等级 not in exc  and i.名称 not in excName:
                if i.是否主动 == 1:
                    i.恢复 += x


    def 单技能加成(self, 名称: str, 倍率=1.0, CD=1.0, lv=0) -> None:
        i = self.get_skill_by_name(名称)
        i.等级加成(lv, char=self)
        if i.是否主动 == 1:
            i.CDR *= CD

    def set_individuation(self, info):
        info['char_optiopns'] = []
        info['char_optiopns'].append({
            "name": '三觉绑定：',
            "option": ["一次觉醒","二次觉醒"]
        })

    def 职业特殊设置(self):
        self.get_skill_by_name("三次觉醒").关联技能= [self.get_skill_by_name('一次觉醒').名称 if self.get_individuation(0) == 0 else self.get_skill_by_name('二次觉醒').名称]
        pass