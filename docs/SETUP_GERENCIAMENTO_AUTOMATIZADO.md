# 🚀 SETUP COMPLETO - GERENCIAMENTO AUTOMATIZADO

**Paulo César M. Sousa Jr.**  
**Data:** 27 Novembro 2025  
**Início das Atividades:** 28 Novembro 2025 às 9h  
**Tempo de Setup:** 50 minutos  
**Custo:** R$ 0/mês

---

## 🎯 VISÃO GERAL DO SISTEMA

### Stack Tecnológico (100% Free)

```
Google Calendar ←→ Notion Database ←→ Google Tasks
        ↓              ↓                    ↓
    Make.com (automação - free tier)
        ↓              ↓                    ↓
Samsung S25+   Galaxy Watch8   Email/SMS
```

### Benefícios para TDAH

✅ **Visual Progress Bars** (motivação constante)  
✅ **Notificações Multi-Device** (não esquecer)  
✅ **Break Reminders** (15 min automático)  
✅ **Daily Summary** (email 7am)  
✅ **Color-Coded Tasks** (fácil identificação)

---

## ⏱️ CRONOGRAMA DE SETUP (50 MINUTOS)

### FASE 1: Preparação (10 min) - FAÇA AGORA

**[0-5 min] Contas & Acessos**
- [ ] Confirmar login Google (paulocesarsousa@gmail.com)
- [ ] Abrir Notion no navegador
- [ ] Criar conta Make.com (https://make.com) - FREE

**[5-10 min] Downloads & Instalações**
- [ ] Notion mobile (Samsung Store) - se não tiver
- [ ] Google Calendar app - verificar atualizado
- [ ] Google Tasks app - verificar atualizado

---

### FASE 2: Notion Setup (15 min)

**[10-15 min] Importar Template Notion**

Vou fornecer um link de template Notion que você vai duplicar.

**Passos:**
1. Abrir Notion
2. Clicar no link do template (vou gerar abaixo)
3. Clicar "Duplicate" no canto superior direito
4. Renomear para "Career Accelerator - Tracker"

**Estrutura do Template:**
```
Career Accelerator - Tracker
├── 📅 Timeline View (visual calendar)
├── ✅ Kanban Board (To Do → Doing → Done)
├── 📊 Dashboard (progress metrics)
├── 📋 Daily Checklist
└── 🎯 Weekly Goals
```

**[15-20 min] Configurar Database**

Na database principal, vou ter as seguintes colunas:

| Campo | Tipo | Propósito |
|-------|------|-----------|
| Task | Title | Nome da tarefa |
| Status | Select | To Do / Doing / Done |
| Date | Date | Quando fazer |
| Duration | Number | Horas estimadas |
| Category | Select | Snowflake / DBT / Portfolio / etc |
| Priority | Select | Alta / Média / Baixa |
| Progress | Number | % conclusão (0-100) |
| Notes | Text | Anotações |

**[20-25 min] Popular com Dados Iniciais**

Vou fornecer CSV para importar todas as 25 dias de tarefas.

Você vai:
1. Baixar CSV que vou criar
2. No Notion: Click "..." → Import → CSV
3. Mapear colunas
4. Confirmar import

---

### FASE 3: Google Calendar Import (10 min)

**[25-30 min] Importar Eventos**

Vou criar arquivo `.ics` (Google Calendar format) com todos os blocos de tempo.

**Passos:**
1. Abrir Google Calendar (https://calendar.google.com)
2. Settings (engrenagem) → Import & Export
3. Import → Select file (.ics que vou criar)
4. Escolher calendar: "Career Transition"
5. Import

**[30-35 min] Configurar Notificações**

Para cada evento:
1. Edit event defaults (Settings)
2. Add notification: 15 minutes before (Push)
3. Add notification: At time of event (Email)
4. Save

---

### FASE 4: Make.com Automação (15 min)

**[35-40 min] Conectar Notion → Google Calendar**

**Passo 1: Criar conta Make.com**
1. https://make.com/en/register
2. Sign up with Google (paulocesarsousa@gmail.com)
3. Free plan (1000 operations/month)

**Passo 2: Create Scenario**
1. Click "Create a new scenario"
2. Add modules:
   - **Trigger:** Notion - Watch Database Items
   - **Action:** Google Calendar - Create Event

**Passo 3: Configure Trigger**
1. Connect Notion account
2. Select database: "Career Accelerator - Tracker"
3. Filter: Status = "To Do" OR "Doing"

**Passo 4: Configure Action**
1. Connect Google account
2. Calendar: "Career Transition"
3. Map fields:
   - Summary: Notion "Task"
   - Start Time: Notion "Date"
   - Duration: Notion "Duration" (hours)
   - Description: Notion "Notes"

**Passo 5: Test & Activate**
1. Click "Run once" (test)
2. Verify event created in Google Calendar
3. Click "Scheduling" → Turn ON
4. Set to run: Every 1 hour

**[40-45 min] Criar Automação de Daily Summary**

**Scenario 2: Daily Email Report**

1. New scenario
2. Add modules:
   - **Trigger:** Schedule (every day 7am)
   - **Action:** Notion - Search Objects (today's tasks)
   - **Action:** Gmail - Send Email

3. Configure email:
   ```
   To: paulocesarsousa@gmail.com
   Subject: 🎯 Seu Plano de Hoje - {{formatDate(now, "DD/MM/YYYY")}}
   
   Bom dia, Paulo!
   
   Suas tarefas para hoje:
   
   {{Notion tasks list}}
   
   Total de horas: {{sum duration}}
   
   Vamos com tudo! 🚀
   ```

4. Activate scenario

**[45-50 min] Criar Progress Reminder**

**Scenario 3: Afternoon Check-in**

1. New scenario
2. Trigger: Schedule (every day 3pm)
3. Actions:
   - Notion: Count completed tasks today
   - Gmail: Send progress email
   
Email template:
```
Olá Paulo,

Progresso de hoje:
✅ Completado: {{completed}} tarefas
⏳ Pendente: {{remaining}} tarefas
📊 % do dia: {{percentage}}%

{{if behind schedule}}
⚠️ Você está um pouco atrasado. Foco!
{{else}}
🎉 Parabéns! Você está no ritmo!
{{end}}

Continue firme! 💪
```

---

### FASE 5: Samsung Integration (10 min)

**[50-55 min] Configurar Galaxy S25+**

**1. Samsung Calendar Sync**
- Abrir Samsung Calendar app
- Settings → Accounts → Add Google account
- Select: paulocesarsousa@gmail.com
- Sync: ON
- Sync frequency: Every 15 minutes

**2. Google Tasks Widget**
- Long press home screen
- Widgets → Google Tasks
- Add "My Tasks" widget (4x2)
- Place on main screen

**3. Bixby Routines (AUTOMAÇÃO TDAH)**

**Routine 1: Morning Kickstart**
```
IF: Time is 9:00 AM (Monday-Friday)
THEN:
- Open Notion app
- Show notification: "Bom dia! Hora de começar 🚀"
- Set Do Not Disturb (except calls)
```

**Routine 2: Break Reminder**
```
IF: Every 2 hours (9am-7pm, Monday-Friday)
THEN:
- Vibrate watch
- Show notification: "Break time! Descanse 15 min ☕"
- Open Samsung Health (stretch suggestions)
```

**Routine 3: End of Day Review**
```
IF: Time is 7:00 PM (Monday-Friday)
THEN:
- Open Notion Dashboard
- Show notification: "Revise seu progresso de hoje 📊"
```

**[55-60 min] Configurar Galaxy Watch8**

**1. Sync Calendars**
- Open Galaxy Wearable app on phone
- Watch settings → Notifications → Calendar
- Enable: All events
- Priority: High

**2. Task Reminders**
- Galaxy Wearable → Apps → Samsung Reminder
- Sync with Google Tasks: ON

**3. Quick Access**
- Watch face: Add Calendar complication
- Swipe right: Add Tasks widget

---

## 📊 VISUALIZAÇÃO GRÁFICA - NOTION DASHBOARD

### Dashboard Automático (Já no Template)

**Widgets que terão:**

**1. Progress Bars**
```
┌─────────────────────────────────────────┐
│  Progresso Geral do Plano (25 dias)    │
├─────────────────────────────────────────┤
│  ████████████░░░░░░░░░░░ 48% (12/25)   │
└─────────────────────────────────────────┘

┌─────────────────────────────────────────┐
│  Progresso de Hoje (9 horas)           │
├─────────────────────────────────────────┤
│  ██████░░░░░░░░░░░░░░░░░ 33% (3/9h)    │
└─────────────────────────────────────────┘
```

**2. Status Cronograma**
```
┌─────────────────────────────────────────┐
│  Status: ✅ NO PRAZO                    │
├─────────────────────────────────────────┤
│  Dias restantes: 13                     │
│  Horas completadas: 54/225              │
│  Taxa conclusão: 24%/dia (meta: 20%)   │
│  Projeção: Concluir em 22/12 (3 dias   │
│            antes do prazo!) 🎉          │
└─────────────────────────────────────────┘
```

**3. Breakdown por Categoria**
```
┌─────────────────────────────────────────┐
│  Snowflake:  ████████░░ 80% (12/15h)   │
│  Databricks: ██░░░░░░░░ 20% (2/10h)    │
│  Portfolio:  ████░░░░░░ 40% (8/20h)    │
│  LinkedIn:   ░░░░░░░░░░  0% (0/5h)     │
└─────────────────────────────────────────┘
```

**4. Próximas Tarefas (Hoje)**
```
┌─────────────────────────────────────────┐
│  🔴 AGORA (9h-11h): Snowflake Badge 1  │
│  🟡 DEPOIS (11h-13h): Mini-Projeto SQL │
│  🟢 TARDE (14h-17h): Badge 2 Inicio    │
└─────────────────────────────────────────┘
```

---

## 📅 CRONOGRAMA AJUSTADO (28 NOV - 22 DEZ)

### Semana 1: 28 Nov - 4 Dez (9h/dia × 5 dias = 45h)

| Dia | Data | Foco | Horas | Entregas |
|-----|------|------|-------|----------|
| **Qui** | 28/11 | Snowflake Architecture + Setup | 9h | Badge 1: 50% |
| **Sex** | 29/11 | Snowflake Data Loading | 9h | Badge 1: 100% ✅ |
| **Sáb** | 30/11 | *(Opcional)* Revisão + Adiantamento | 8h | Buffer |
| **Dom** | 1/12 | *(Opcional)* Portfolio work | 8h | Lineage +20% |
| **Seg** | 2/12 | Snowflake Performance | 9h | Badge 2: 60% |
| **Ter** | 3/12 | Snowflake + DBT Integration | 9h | Badge 2: 100% ✅ |
| **Qua** | 4/12 | Snowflake Advanced + Cert Prep | 9h | Badge 3: 80% |

**Total Semana 1:** 45h (seg-sex) + 16h (opcional fim de semana) = **61h potencial**

---

### Detalhamento DIA 1 - 28 Novembro (Quinta)

**Total: 9 horas | Início: 9h | Fim: 19h**

#### Bloco 1: Manhã (9h - 13h) = 4 horas

**9h00 - 10h30 (1.5h): Snowflake Architecture Overview**
- [ ] [30min] Vídeo: Snowflake Architecture Explained
- [ ] [30min] Leitura: Docs oficiais - Virtual Warehouses
- [ ] [30min] Leitura: Storage vs Compute separation
- **Entrega:** Notes resumidas (Notion)

*Break 15 min (10h30-10h45)*

**10h45 - 13h00 (2.25h): Setup + Badge 1 Início**
- [ ] [30min] Criar Snowflake trial account
- [ ] [15min] Configurar warehouse inicial
- [ ] [1h40min] Badge 1: Data Warehousing Workshop (Parte 1)
  - Load sample data
  - Execute first queries
  - Understand query profile
- **Entrega:** Snowflake account ativo + 30% Badge 1

*Almoço (13h00-14h00)*

---

#### Bloco 2: Tarde (14h - 19h) = 5 horas

**14h00 - 16h00 (2h): Badge 1 Continuação**
- [ ] [2h] Data Warehousing Workshop (Parte 2)
  - Semi-structured data (JSON)
  - File formats
  - Stages (internal/external)
- **Entrega:** 70% Badge 1

*Break 15 min (16h00-16h15)*

**16h15 - 18h15 (2h): Badge 1 Finalização**
- [ ] [1h30min] Completar todos exercises
- [ ] [30min] Quiz final + obter badge
- **Entrega:** Badge 1: 100% ✅

*Break 15 min (18h15-18h30)*

**18h30 - 19h00 (30min): Documentação & Reflection**
- [ ] [15min] Atualizar Notion (check tasks, update progress)
- [ ] [15min] Notes: 3 key learnings de hoje
- **Entrega:** Daily log completo

---

### Template de Checklist Diário (Notion)

```markdown
# 📅 Dia 1 - 28 Novembro 2025

## 🎯 Objetivo do Dia
Completar Snowflake Badge 1 + Setup environment

## ✅ Checklist Manhã (9h-13h)

### Bloco 1 (9h-10h30) - 1.5h
- [ ] Vídeo: Snowflake Architecture (30min)
- [ ] Docs: Virtual Warehouses (30min)
- [ ] Docs: Storage/Compute (30min)
- [ ] Notes resumidas (Notion)

**Break 15min** ☕

### Bloco 2 (10h45-13h) - 2.25h
- [ ] Criar trial account (30min)
- [ ] Setup warehouse (15min)
- [ ] Badge 1 - Parte 1 (1h40min)

**Almoço 1h** 🍽️

## ✅ Checklist Tarde (14h-19h)

### Bloco 3 (14h-16h) - 2h
- [ ] Badge 1 - Parte 2 (2h)

**Break 15min** ☕

### Bloco 4 (16h15-18h15) - 2h
- [ ] Badge 1 - Finalização (1h30min)
- [ ] Quiz + obter badge (30min)

**Break 15min** ☕

### Bloco 5 (18h30-19h) - 30min
- [ ] Atualizar Notion
- [ ] Daily reflection

## 📊 Progresso

- **Horas planejadas:** 9h
- **Horas completadas:** ____ h
- **% conclusão:** ____ %
- **Status:** 🟢 No prazo / 🟡 Atrasado / 🔴 Crítico

## 📝 Learnings de Hoje

1. Learning 1
2. Learning 2
3. Learning 3

## 🚧 Blockers / Desafios

- [Se houver]

## 🎉 Wins do Dia

- [Celebrar pequenas vitórias]

---

## 📅 Preparação para Amanhã

- [ ] Revisar material Badge 2
- [ ] Setup: ____ (se necessário)
```

---

## 🎨 CSV PARA IMPORTAR NO NOTION

Vou criar arquivo separado com todas as tarefas dos 25 dias.

**Preview (primeiros 5 dias):**

```csv
Task,Status,Date,Duration,Category,Priority,Notes
"Snowflake Architecture Overview",To Do,2025-11-28,1.5,Snowflake,Alta,"Vídeo + docs oficiais"
"Criar Snowflake trial",To Do,2025-11-28,0.5,Snowflake,Alta,"Account setup"
"Badge 1: Data Warehousing (Parte 1)",To Do,2025-11-28,1.75,Snowflake,Alta,"Load data + queries"
"Badge 1: Data Warehousing (Parte 2)",To Do,2025-11-28,2,Snowflake,Alta,"Semi-structured data"
"Badge 1: Finalização + Quiz",To Do,2025-11-28,2,Snowflake,Alta,"Complete + badge"
"Daily Documentation",To Do,2025-11-28,0.5,Admin,Média,"Notion update"
...
```

(Arquivo completo com 100+ tasks será gerado separadamente)

---

## 📧 TEMPLATES DE EMAIL (Make.com)

### Template 1: Daily Morning Email (7am)

```
Assunto: 🎯 Seu Plano para Hoje - {{formatDate(now, "DD/MM/YYYY")}}

Bom dia, Paulo! ☀️

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 QUINTA-FEIRA, 28 DE NOVEMBRO
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🎯 OBJETIVO DE HOJE:
Completar Snowflake Badge 1 + Setup environment

✅ SUAS TAREFAS (9 horas total):

MANHÃ (9h-13h):
├─ [1.5h] Snowflake Architecture Overview
├─ [0.5h] Criar trial account
└─ [1.75h] Badge 1 - Parte 1

TARDE (14h-19h):
├─ [2h] Badge 1 - Parte 2
├─ [2h] Badge 1 - Finalização + Quiz
└─ [0.5h] Documentação diária

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PROGRESSO GERAL:

Plano 25 dias: [████░░░░░░░░░░░░░░] 20% (5/25 dias)
Horas total: 45/225h completadas
Status: 🟢 NO PRAZO

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💪 MOTIVAÇÃO DO DIA:

"Cada hora investida hoje é um passo mais perto
do seu objetivo. Você consegue!"

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Lembretes importantes:
⏰ Breaks de 15 min a cada 2h
🍽️ Almoço: 13h-14h
💧 Hidratação constante

Vamos com tudo! 🚀

---
📱 Abrir Notion Dashboard: [Link]
📅 Ver Calendar: [Link]
```

### Template 2: Afternoon Progress Check (15h)

```
Assunto: 📊 Check-in de Progresso - {{time}}

Olá Paulo,

Como está indo seu dia?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 PROGRESSO DE HOJE:

Completado: ✅ {{completed_tasks}} tarefas
Pendente: ⏳ {{remaining_tasks}} tarefas
Horas feitas: {{hours_done}}/9h
% do dia: {{percentage}}%

{{#if on_track}}
🎉 Parabéns! Você está no ritmo planejado!
Continue assim! 💪
{{else if slightly_behind}}
⚠️ Você está um pouco atrasado, mas nada grave.
Foco nas próximas 4 horas! 🎯
{{else}}
🚨 Atenção! Você está bastante atrasado.
Vamos priorizar as tarefas críticas! 🔥
{{/if}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⏰ RESTANTE DO DIA (14h-19h):

{{remaining_tasks_list}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💡 Dica: Não esqueça dos breaks de 15 min!

Vamos finalizar o dia com chave de ouro! 🔑

---
📱 Atualizar Notion: [Link]
```

### Template 3: End of Day Summary (19h30)

```
Assunto: 🎯 Resumo do Dia - {{formatDate(now, "DD/MM/YYYY")}}

Boa noite, Paulo!

Hora de revisar o que você conquistou hoje! 🌙

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ CONQUISTAS DE HOJE:

Tasks completadas: {{completed_count}}
Horas trabalhadas: {{hours_worked}}h
% conclusão: {{completion_percentage}}%

{{completed_tasks_list}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 STATUS CRONOGRAMA:

{{#if ahead_schedule}}
🎉 PARABÉNS! Você está {{days_ahead}} dia(s) adiantado!
Continue nesse ritmo incrível! 🚀
{{else if on_schedule}}
✅ Perfeito! Você está exatamente no prazo!
Mantenha a consistência! 💪
{{else}}
⚠️ Atenção: {{days_behind}} dia(s) de atraso.
Vamos recuperar amanhã! 🔥
{{/if}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📅 AMANHÃ ({{tomorrow_date}}):

Objetivo: {{tomorrow_goal}}

Primeiras tarefas:
{{tomorrow_first_tasks}}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💭 REFLEXÃO:

Reserve 5 minutos para responder no Notion:
1. Qual foi meu maior aprendizado hoje?
2. Qual foi meu maior desafio?
3. O que posso melhorar amanhã?

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Descanse bem! Amanhã é um novo dia de conquistas! 😴

---
📱 Preencher reflexão: [Link Notion]
```

---

## 📱 BIXBY ROUTINES - CÓDIGO DE CONFIGURAÇÃO

### Routine 1: Morning Kickstart

```json
{
  "routineName": "Career Kickstart - Manhã",
  "triggers": [
    {
      "type": "time",
      "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "time": "09:00"
    }
  ],
  "actions": [
    {
      "type": "notification",
      "title": "🚀 Bom dia, Paulo!",
      "message": "Hora de começar! Seu primeiro bloco é Snowflake Architecture.",
      "priority": "high"
    },
    {
      "type": "openApp",
      "app": "Notion"
    },
    {
      "type": "setMode",
      "mode": "Do Not Disturb",
      "exceptions": ["calls"]
    },
    {
      "type": "watchNotification",
      "message": "Começar agora! 💪"
    }
  ]
}
```

### Routine 2: Break Reminder (A cada 2h)

```json
{
  "routineName": "Career Break Reminder",
  "triggers": [
    {
      "type": "time",
      "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "times": ["11:00", "13:00", "16:00", "18:00"]
    }
  ],
  "actions": [
    {
      "type": "watchVibrate",
      "pattern": "gentle"
    },
    {
      "type": "notification",
      "title": "⏸️ Break Time!",
      "message": "Descanse 15 minutos. Hidrate-se! 💧",
      "icon": "coffee"
    },
    {
      "type": "openApp",
      "app": "Samsung Health",
      "action": "stretchSuggestions"
    }
  ]
}
```

### Routine 3: End of Day Review

```json
{
  "routineName": "Career Day Review",
  "triggers": [
    {
      "type": "time",
      "days": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
      "time": "19:00"
    }
  ],
  "actions": [
    {
      "type": "notification",
      "title": "📊 Hora da Revisão!",
      "message": "Revise seu progresso de hoje no Notion Dashboard.",
      "action": "openNotion"
    },
    {
      "type": "watchNotification",
      "message": "Revisar progresso 📊",
      "vibrate": true
    },
    {
      "type": "setMode",
      "mode": "Normal"
    }
  ]
}
```

---

## ✅ TUTORIAL PASSO-A-PASSO (O QUE VOCÊ FAZ)

### AGORA - PRÓXIMOS 50 MINUTOS

#### ✅ PASSO 1: Organizar Arquivos (5 min)

1. Abrir terminal no Mac/Windows
2. Navegar para pasta Downloads
3. Executar script de organização:

**Mac/Linux:**
```bash
cd ~/Downloads
bash organize_files.sh
```

**Windows (Git Bash):**
```bash
cd /c/Users/SeuUsuario/Downloads
bash organize_files.sh
```

4. Verificar arquivos movidos:
```bash
cd ~/paulo-career-accelerator
ls -la docs/planning/
```

---

#### ✅ PASSO 2: Notion Setup (15 min)

**[Minuto 5-10] Importar Template**

1. Abrir: https://notion.so
2. Login: paulocesarsousa@gmail.com
3. Clicar no link do template (vou gerar)
4. "Duplicate to your workspace"
5. Renomear: "Career Accelerator - Master Tracker"

**[Minuto 10-15] Importar CSV de Tarefas**

1. Baixar CSV (vou criar arquivo separado)
2. No Notion, abrir database "Tasks"
3. Click "..." (top right) → Import → CSV
4. Upload arquivo CSV
5. Map columns:
   - Column 1 → Task
   - Column 2 → Status
   - Column 3 → Date
   - (etc)
6. Import

**[Minuto 15-20] Verificar Dashboard**

1. Abrir view "Dashboard"
2. Verificar progress bars funcionando
3. Pin dashboard (bookmark)
4. Adicionar atalho mobile (share → add to home screen)

---

#### ✅ PASSO 3: Google Calendar (10 min)

**[Minuto 20-25] Importar Eventos**

1. Abrir: https://calendar.google.com
2. Settings (⚙️) → Import & Export
3. Select file: `career-accelerator-calendar.ics` (vou criar)
4. Select calendar: Create new "Career Transition"
5. Import

**[Minuto 25-30] Configurar Notificações**

1. Settings → Event settings
2. Default notifications:
   - Add: 15 minutes before (Notification)
   - Add: At time of event (Email)
3. Save

**[Minuto 30] Sync com Samsung Calendar**

1. Abrir Samsung Calendar no celular
2. Menu → Settings → Sync
3. Add account → Google
4. Select: paulocesarsousa@gmail.com
5. Sync frequency: 15 minutes
6. Done

---

#### ✅ PASSO 4: Make.com Automação (15 min)

**[Minuto 30-35] Criar Conta**

1. Abrir: https://make.com/en/register
2. Sign up with Google (paulocesarsousa@gmail.com)
3. Select plan: FREE
4. Verify email
5. Login

**[Minuto 35-45] Scenario 1: Notion → Calendar Sync**

1. Dashboard → Create new scenario
2. Add module: Notion → Watch Database Items
   - Click "Add" → Login Notion
   - Select workspace
   - Database: "Career Accelerator - Master Tracker"
   - Trigger: On new or updated item
   - Filter: Status = "To Do" OR "Doing"

3. Add module: Google Calendar → Create/Update Event
   - Click "Add" → Login Google
   - Calendar: "Career Transition"
   - Map fields:
     ```
     Summary: {{Task}}
     Start: {{Date}} {{formatDate(Date, "09:00:00")}}
     End: {{Date}} {{addHours(Duration, Start)}}
     Description: {{Notes}}
     ```

4. Save scenario (name: "Notion to Calendar Sync")
5. Turn ON (toggle switch)
6. Scheduling: Every 1 hour

**[Minuto 45-50] Scenario 2: Daily Morning Email**

1. New scenario
2. Add module: Tools → Schedule
   - Type: Every day
   - Time: 07:00 (UTC-3)
   - Days: Monday-Friday

3. Add module: Notion → Search Objects
   - Database: "Career Accelerator"
   - Filter: Date = Today AND Status != "Done"

4. Add module: Gmail → Send Email
   - To: paulocesarsousa@gmail.com
   - Subject: `🎯 Seu Plano para Hoje - {{formatDate(now, "DD/MM/YYYY")}}`
   - Body: (copiar template acima)

5. Save & Activate

---

#### ✅ PASSO 5: Samsung Config (10 min)

**[Minuto 50-55] Galaxy S25+ Widgets**

1. Long press home screen
2. Widgets
3. Add: Google Tasks (4x2)
4. Add: Notion widget (4x4)
5. Arrange on main screen

**[Minuto 55-60] Bixby Routines**

1. Open Bixby Routines app
2. "+" → Create new routine
3. Name: "Career Kickstart - Manhã"
4. Triggers:
   - Time: 9:00 AM
   - Days: Monday-Friday
5. Actions:
   - Notification: "Bom dia! Hora de começar 🚀"
   - Open app: Notion
   - Do Not Disturb: ON (except calls)
6. Save

Repetir para outras 2 routines (Break, End of Day)

---

## ✅ CHECKLIST FINAL - TUDO CONFIGURADO?

Antes de começar amanhã (28/11 às 9h), verificar:

**Notion:**
- [ ] Template duplicado
- [ ] CSV importado (100+ tasks)
- [ ] Dashboard funcionando
- [ ] Mobile app instalado

**Google Calendar:**
- [ ] Eventos importados (.ics)
- [ ] Notificações configuradas (15 min + email)
- [ ] Sync com Samsung Calendar

**Google Tasks:**
- [ ] Widget na home screen
- [ ] Sync ativo

**Make.com:**
- [ ] Conta criada (free)
- [ ] Scenario 1: Notion → Calendar (ON)
- [ ] Scenario 2: Daily email (ON)
- [ ] Test: Recebeu email de teste?

**Samsung S25+:**
- [ ] Widgets adicionados (Tasks, Notion)
- [ ] Bixby Routines criadas (3 routines)
- [ ] Calendar sync verificado

**Samsung Watch8:**
- [ ] Calendar sync
- [ ] Notificações habilitadas
- [ ] Complications adicionadas

**Email de Teste:**
- [ ] Enviar email teste Make.com
- [ ] Verificar recebimento no Gmail
- [ ] Verificar notificação no celular

---

## 🚀 AMANHÃ - 28 NOVEMBRO - DIA 1

### Às 9h00 (Quinta-feira):

**O que vai acontecer automaticamente:**

1. **7:00 AM** - Email chega: "Seu Plano para Hoje"
2. **9:00 AM** - Notification no celular: "Bom dia! Hora de começar 🚀"
3. **9:00 AM** - Watch vibra suavemente
4. **9:00 AM** - Notion abre automaticamente (Bixby)
5. **9:00 AM** - Do Not Disturb ativado (exceto calls)

**O que você faz:**

1. Abrir Notion Dashboard (já aberto pelo Bixby)
2. Ver checklist do dia
3. Começar primeira tarefa: "Snowflake Architecture Overview"
4. Work 1.5h
5. **10:30 AM** - Break 15 min (lembrete automático)
6. Continue...

---

## 📊 MÉTRICAS QUE VOCÊ VAI VER

### No Notion Dashboard:

```
┌────────────────────────────────────────────┐
│        PROGRESSO GERAL (25 DIAS)           │
├────────────────────────────────────────────┤
│  Dia 1/25 (4%)                             │
│  [█░░░░░░░░░░░░░░░░░░░░░░░░] 4%          │
│                                            │
│  Horas: 0/225                              │
│  Status: 🟢 Iniciando                      │
│  Projeção: 22/Dez (no prazo)               │
└────────────────────────────────────────────┘

┌────────────────────────────────────────────┐
│          PROGRESSO DE HOJE                 │
├────────────────────────────────────────────┤
│  Meta: 9 horas                             │
│  Completado: 0h                            │
│  [░░░░░░░░░░░░░░░░░░░░░░░░] 0%           │
│                                            │
│  Próxima tarefa:                           │
│  🔴 Snowflake Architecture (1.5h)          │
│     Iniciar às 9h                          │
└────────────────────────────────────────────┘
```

---

## 💡 DICAS PARA TDAH

### Como Manter Foco:

**1. Pomodoro Modificado**
- Work: 90 min (não 25 min padrão)
- Break: 15 min (fixo)
- Razão: Tasks complexas precisam "flow state"

**2. Visual Cues**
- Progress bars (satisfação imediata)
- Color coding (red = agora, yellow = próximo, green = feito)
- Checkboxes (dopamina ao completar)

**3. Accountabilidade Externa**
- Emails automáticos 2x/dia
- Watch vibra (physical reminder)
- Claude check-in (conversar progresso)

**4. Eliminar Distrações**
- Do Not Disturb automático
- Phone face down
- Single task focus (não multitask)

**5. Celebrar Pequenas Vitórias**
- Cada task completada = ✅ visual
- End of day email = recap wins
- Weekly: Treat yourself (se meta atingida)

---

## 🆘 TROUBLESHOOTING

### "Make.com não está sincronizando"

**Possíveis causas:**
1. Scenario OFF → Turn ON
2. Notion integration expirou → Reconnect
3. Free tier limit (1000 ops) → Check usage

**Solução:**
1. Make.com dashboard → Scenarios
2. Check status (verde = ON)
3. Click scenario → Execution history
4. Ver errors (se houver)

---

### "Não recebi email de manhã"

**Checklist:**
1. Make.com scenario ativo? (check dashboard)
2. Horário correto? (7am UTC-3)
3. Email certo? (paulocesarsousa@gmail.com)
4. Check spam folder
5. Test: Run scenario manually

---

### "Progress bar não atualiza"

**Solução:**
1. Notion → Refresh page (F5)
2. Database → Check formulas
3. Progress field = Number type?
4. Formula: `prop("Completed Tasks") / prop("Total Tasks") * 100`

---

## 📞 SUPORTE

**Se precisar de ajuda:**

1. **Durante setup:** 
   - Pergunte aqui no chat (estou disponível)
   - Screenshot do erro

2. **Durante execução:**
   - Daily check-in comigo (2x/dia)
   - Troubleshooting section acima

3. **Emergência:**
   - Simplificar: Usar só Google Calendar + Tasks (sem Make.com)
   - Você não perde nada, só automação

---

## ✅ PRÓXIMAS AÇÕES (DEPOIS DO SETUP)

### Hoje ainda (27/11):

1. **URGENTE: Atualizar Currículo (2h)**
   - Vou criar documento separado
   - Versão ATS-optimized
   - Versão visual

2. **Finalizar setup (50 min)**
   - Seguir este tutorial
   - Verificar checklist final

3. **Descansar bem**
   - Amanhã começa jornada intensa
   - 9 horas de foco

### Amanhã (28/11) - 9h:

1. **Acordar 7h30**
   - Ler email "Plano do Dia"
   - Café da manhã leve
   - Hidratação

2. **9h00 - START**
   - Notification automática
   - Abrir Notion
   - Começar Snowflake Architecture

3. **19h00 - END**
   - Review automático
   - Preencher reflection
   - Descansar

---

## 🎉 VOCÊ ESTÁ PRONTO!

Paulo, depois de completar este setup de 50 minutos, você terá:

✅ **Sistema totalmente automatizado** (R$ 0/mês)  
✅ **Notificações multi-device** (Phone + Watch)  
✅ **Progress tracking visual** (Notion Dashboard)  
✅ **Accountability automático** (Emails 2x/dia)  
✅ **TDAH-friendly** (lembretes, breaks, progress bars)  
✅ **Tudo sincronizado** (Notion ↔ Calendar ↔ Tasks)

**Agora é só executar!**

Amanhã às 9h, você recebe:
- Email com plano do dia
- Notification no celular
- Vibração no Watch
- Notion abrindo automaticamente

**Você só precisa começar a estudar.** 🚀

**O sistema cuida do resto.**

---

**Última atualização:** 27 Novembro 2025  
**Início:** 28 Novembro 2025 às 9h  
**Fim estimado:** 22 Dezembro 2025  
**Total:** 25 dias de transformação

---

> "O sistema está pronto. Agora é só confiar no processo e executar, um dia de cada vez."

**Vamos juntos, Paulo! Você consegue!** 💪🚀
