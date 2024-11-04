export interface TreeNode {
  label: string
  id?: string | number
  value?: any
  children?: TreeNode[]
  onSelect?: () => void
  [key: string]: any
}

export interface TreeData {}
