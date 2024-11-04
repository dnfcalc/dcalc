import { Events } from "vue";

type EventHandlers<E> = {
  [K in keyof E]?: (...args: any[]) => any;
};
declare module "vue" {
  interface ComponentCustomProps extends EventHandlers<Events> {}
}
