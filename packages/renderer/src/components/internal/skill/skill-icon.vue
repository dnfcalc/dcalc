<script lang="tsx">
import { defineComponent, ref } from "vue"
import { onClickOutside } from "@vueuse/core"
export default defineComponent({
  name: "SkillIcon",
  components: {},
  props: {
    skill: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    function increaseSkillLv(skill: any) {
      return () => {
        if (skill.learn < skill.master) {
          skill.learn++
        }
      }
    }
    function increaseSkillLvToMax(skill: any) {
      return () => {
        skill.learn = skill.learnMax > 0 && skill.learn < skill.learnMax ? skill.learnMax : skill.master
      }
    }

    function reduceSkillLv(skill: any) {
      return () => {
        if (skill.learn > skill.default) {
          skill.learn--
        }
      }
    }
    function reduceSkillLvToMin(skill: any) {
      return () => {
        skill.learn = skill.learnMax > 0 && skill.learn > skill.learnMax ? skill.learnMax : skill.default
      }
    }

    const show = ref(false)
    function showOptions() {
      if ((props.skill.sp && props.skill.sp != 0) || props.skill.tp != null) {
        show.value = true
      }
    }

    const skillIconRef = ref<HTMLElement>()
    onClickOutside(skillIconRef, () => (show.value = false))

    function lvRender(skill: any) {
      const t = skill ? skill.learn == skill.master ? <span class="M">M</span> : <span class="lv">Lv</span> : <span></span>
      return skill ? (
        <span>
          {t}
          <span class="num">{skill.learn}</span>
        </span>
      ) : (
        <span></span>
      )
    }

    function optionRender(skill: any) {
      return (
        <div class="skill-option-panel">
          <div class="skill-option-item" onClick={reduceSkillLvToMin(skill)}>
              &lt;&lt;
          </div>
          <div class="skill-option-item" onClick={reduceSkillLv(skill)}>
              -
          </div>
          <div class="skill-lv">{lvRender(skill)}</div>
          <div class="skill-option-item" onClick={increaseSkillLv(skill)}>
              +
          </div>
          <div class="skill-option-item" onClick={increaseSkillLvToMax(skill)}>
              &gt;&gt;
          </div>
        </div>
      )
    }

    return {
      renderTemp: () => {
        return (
          <div ref={skillIconRef} class={["skill-icon"].concat(show.value ? "active" : "", props.skill.tp != null ? "with-tp" : "")} onClick={showOptions}>
            <div class={["img"].concat([props.skill.learn > props.skill.learnMax ? "red" : ""])}>
              <img src={props.skill.icon} />
              <div class="tp-lv" v-show={props.skill.tp}>
                {props.skill.tp?.learn}
              </div>
            </div>
            <div class="skill-lv">{lvRender(props.skill)}</div>
            {
              // <div class="skill-lv" v-show={props.skill.tp}>{lvRender(props.skill.tp)}</div>
            }
            <div class="skill-options" v-show={show.value}>
              {optionRender(props.skill)}
              {props.skill.tp ? optionRender(props.skill.tp) : null}
            </div>
          </div>
        )
      }
    }
  },
  render() {
    return this.renderTemp()
  }
})
</script>

<style scoped lang="scss">
  .skill-icon {
    display: inline-block;
    width: 36px;
    height: 56px; // 56
    border: 1px solid #000;
    border-radius: 2px;
    background-color: #2f2f2f;
    position: relative;

    &.active {
      border-color: #c9984a;

      &:hover {
        border-color: #c9984a;
      }
    }

    &.with-tp {
      height: 56px; //74px;
    }

    &:hover {
      border-color: #64add0;
    }

    > .img {
      margin: 2px 2px 2px 2px;
      display: block;
      width: 30px;
      height: 30px;
      border: 1px solid #000;
      position: relative;

      > img {
        width: 30px;
        height: 30px;
      }

      .tp-lv {
        position: absolute;
        color: #d8f479;
        right: 0px;
        top: 0px;
        background-color: #000;
        font-weight: 700;
      }

      &.red {
        &::after {
          background-color: rgba($color: #aa3333, $alpha: 0.3);
          content: "";
          position: absolute;
          width: 100%;
          height: 100%;
          left: 0;
          top: 0;
        }
      }
    }

    .skill-lv {
      margin: 0 5px;
      background-color: #000;
      text-align: center;
      // font-size: 12px;
      height: 18px;
      line-height: 18px;
      width: calc(100% - 4px);
      margin-left: 2px;

      .lv {
        margin-right: 3px;
        color: #fff;
      }

      .M {
        margin-right: 2px;
        border: 1px solid #c6a228;
        border-radius: 3px;
        color: #c6a228;
        display: inline-block;
        height: 10px;
        line-height: 11px;
        padding: 0 1px 0 2px;

        + .num {
          color: #c6a228;
        }
      }

      .num {
        color: #fff;
      }
    }

    .skill-options {
      position: absolute;
      top: 36px;
      left: calc(50% - 67.5px);
      width: calc(97px + 38px);
      border: 1px solid #c9984a;
      z-index: 10;
      background-color: #161616;

      .skill-option-panel {
        height: 24px;
        width: 100%;
        display: flex;

        .skill-option-item {
          width: 18px;
          height: 18px;
          border: 1px solid #4b3a24;
          margin-top: 2px;
          margin-left: 2px;
          color: #b69260;
          text-align: center;
          line-height: 18px;

          &:hover {
            color: #e2d39a;
            border-color: #e2d39a;
          }
        }

        .skill-lv {
          background-color: transparent;
          padding-top: 2px;
          width: 38px;
          text-align: center;
        }
      }
    }
  }
</style>
