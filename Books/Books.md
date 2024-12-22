---

database-plugin: basic

---

```yaml:dbfolder
name: new database
description: new description
columns:
  __file__:
    key: __file__
    id: __file__
    input: markdown
    label: File
    accessorKey: __file__
    isMetadata: true
    skipPersist: false
    isDragDisabled: false
    csvCandidate: true
    position: 1
    isHidden: false
    sortIndex: -1
    width: 172
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: true
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Autor:
    input: select
    accessorKey: Autor
    key: Autor
    id: Autor
    label: Autor
    position: 2
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 177
    options:
      - { label: "Mario Vargas Llosa", value: "Mario Vargas Llosa", color: "hsl(177, 95%, 90%)"}
      - { label: "Imanuel Kant", value: "Imanuel Kant", color: "hsl(216, 95%, 90%)"}
      - { label: "Ozamu Dazai", value: "Ozamu Dazai", color: "hsl(205, 95%, 90%)"}
      - { label: "Franz Kafka", value: "Franz Kafka", color: "hsl(311, 95%, 90%)"}
      - { label: "George Orwell", value: "George Orwell", color: "hsl(189, 95%, 90%)"}
      - { label: "Bradbury", value: "Bradbury", color: "hsl(120, 95%, 90%)"}
      - { label: "Gabriel Garcia marquez", value: "Gabriel Garcia marquez", color: "hsl(113, 95%, 90%)"}
      - { label: "Cortazar", value: "Cortazar", color: "hsl(96, 95%, 90%)"}
      - { label: "Mario Benedetti", value: "Mario Benedetti", color: "hsl(197, 95%, 90%)"}
      - { label: "Hesse", value: "Hesse", color: "hsl(72, 95%, 90%)"}
      - { label: "Fiodor Dostoiewsky", value: "Fiodor Dostoiewsky", color: "hsl(65, 95%, 90%)"}
      - { label: "Lev tolstoi", value: "Lev tolstoi", color: "hsl(308, 95%, 90%)"}
      - { label: "Virginia Woolf", value: "Virginia Woolf", color: "hsl(325, 95%, 90%)"}
      - { label: "Juan Rulfo", value: "Juan Rulfo", color: "hsl(225, 95%, 90%)"}
      - { label: "Jean Paul sartre", value: "Jean Paul sartre", color: "hsl(203, 95%, 90%)"}
      - { label: "Jose Saramago", value: "Jose Saramago", color: "hsl(28, 95%, 90%)"}
      - { label: "Julio Ramon Ribeyro", value: "Julio Ramon Ribeyro", color: "hsl(301, 95%, 90%)"}
      - { label: "Jaime Bayli", value: "Jaime Bayli", color: "hsl(246, 95%, 90%)"}
      - { label: "Ernesto Sabato", value: "Ernesto Sabato", color: "hsl(222, 95%, 90%)"}
      - { label: "Jane Austen", value: "Jane Austen", color: "hsl(235, 95%, 90%)"}
      - { label: "Bukowski", value: "Bukowski", color: "hsl(293, 95%, 90%)"}
      - { label: "Haruki Murakami", value: "Haruki Murakami", color: "hsl(161, 95%, 90%)"}
      - { label: "Albert Camus", value: "Albert Camus", color: "hsl(39, 95%, 90%)"}
      - { label: "Julio Verne", value: "Julio Verne", color: "hsl(248, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Estado:
    input: select
    accessorKey: Estado
    key: Estado
    id: Estado
    label: Estado
    position: 3
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 140
    options:
      - { label: "terminado", value: "terminado", color: "hsl(353, 95%, 90%)"}
      - { label: "No comenzado", value: "No comenzado", color: "hsl(329, 95%, 90%)"}
      - { label: "comenzado", value: "comenzado", color: "hsl(193, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Tipo:
    input: select
    accessorKey: Tipo
    key: Tipo
    id: Tipo
    label: Tipo
    position: 4
    skipPersist: false
    isHidden: false
    sortIndex: -1
    options:
      - { label: "Novela", value: "Novela", color: "hsl(213, 95%, 90%)"}
      - { label: "Ensayo", value: "Ensayo", color: "hsl(355, 95%, 90%)"}
      - { label: "Cuento", value: "Cuento", color: "hsl(323, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Comentarios:
    input: text
    accessorKey: Comentarios
    key: Comentarios
    id: Comentarios
    label: Comentarios
    position: 5
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Puntuacion:
    input: number
    accessorKey: Puntuacion
    key: Puntuacion
    id: Puntuacion
    label: Puntuacion
    position: 6
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Comprado?:
    input: checkbox
    accessorKey: Comprado?
    key: Comprado?
    id: Comprado?
    label: Comprado?
    position: 7
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Prioridad:
    input: number
    accessorKey: Prioridad
    key: Prioridad
    id: Prioridad
    label: Prioridad
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
  Editorial:
    input: select
    accessorKey: Editorial
    key: Editorial
    id: Editorial
    label: Editorial
    position: 100
    skipPersist: false
    isHidden: false
    sortIndex: -1
    width: 136
    options:
      - { label: "Alfaguara", value: "Alfaguara", color: "hsl(135, 95%, 90%)"}
      - { label: "Gredos", value: "Gredos", color: "hsl(294, 95%, 90%)"}
      - { label: "Editorial Textos", value: "Editorial Textos", color: "hsl(35, 95%, 90%)"}
      - { label: "Null", value: "Null", color: "hsl(227, 95%, 90%)"}
    config:
      enable_media_view: true
      link_alias_enabled: true
      media_width: 100
      media_height: 100
      isInline: false
      task_hide_completed: true
      footer_type: none
      persist_changes: false
config:
  remove_field_when_delete_column: false
  cell_size: normal
  sticky_first_column: false
  group_folder_column: 
  remove_empty_folders: false
  automatically_group_files: false
  hoist_files_with_empty_attributes: true
  show_metadata_created: false
  show_metadata_modified: false
  show_metadata_tasks: false
  show_metadata_inlinks: false
  show_metadata_outlinks: false
  show_metadata_tags: false
  source_data: current_folder
  source_form_result: 
  source_destination_path: /
  row_templates_folder: /
  current_row_template: 
  pagination_size: 115
  font_size: 10
  enable_js_formulas: false
  formula_folder_path: /
  inline_default: false
  inline_new_position: last_field
  date_format: yyyy-MM-dd
  datetime_format: "yyyy-MM-dd HH:mm:ss"
  metadata_date_format: "yyyy-MM-dd HH:mm:ss"
  enable_footer: false
  implementation: default
filters:
  enabled: false
  conditions:
```