# -*- coding: utf-8 -*-
################################################################################
#    Author: Don Shan
#
################################################################################
{
    'name': 'OdooCNSh | Self-Hosted Odoo Hosting Platform | Git Branch Environments | '
            'Multi-Tenant Odoo Cloud | Docker | Deploy on Push | Backup & Restore | Web Shell | Odoo SH | odoo.sh',
    'version': '19.0.1.0.0',
    'category': 'Productivity',
    'summary': 'Run your own Odoo cloud on your own Linux servers: Git branch = environment '
               '(production / staging / development), deploy on push, multi-tenant organizations '
               'and roles, staging cloned from production and neutralized, golden template '
               'databases in seconds, idle sleep & auto wake, backups to S3 / SFTP / WebDAV, '
               'live logs, monitoring, web code editor, Web Shell, AI ops assistant, offline install.',
    'description': """
OdooCNSh - Self-Hosted Odoo Hosting Platform
============================================

OdooCNSh is a complete platform to host, deploy and operate many Odoo instances
on your own Linux servers, for integrators, software houses, schools and
companies that want their own Odoo cloud.

Key Features
------------
* **Git branch = environment** - connect GitHub / Gitee repositories; every branch
  becomes a production, staging or development environment. Drag a branch to change
  its stage.
* **Deploy on push** - webhooks or polling deploy staging / development automatically;
  production is deployed with one click. Restart only, update changed modules or
  update all; automatic rollback when the health check fails.
* **Staging from production** - staging databases are cloned from production and
  neutralized (no outgoing mail, no crons, no payments).
* **Golden template databases** - new instances of the same version are ready in
  seconds instead of minutes.
* **Multi-tenant** - organizations, members and roles (owner / developer / tester),
  per-instance access lists, quotas for instances, memory, CPU and databases.
* **Odoo 12 to 19, Community and Enterprise** - official Docker images or build
  from source; Enterprise code mounted read-only from a shared folder.
* **Idle sleep and auto wake** - development instances sleep when unused and wake
  up automatically on the next visit.
* **Backups** - official Odoo zip format, daily automatic backups, retention rules,
  restore to any environment, off-site copies on S3 / OSS / COS / MinIO / SFTP / WebDAV.
* **Live logs and monitoring** - real-time log streaming with filters, CPU, memory,
  network, disk IO, filestore and database size charts.
* **Web code editor** - edit custom modules in the browser (Monaco editor with Odoo
  autocompletion), scaffold modules, upload zips, version history, one-click upgrade.
* **Web Shell** - a terminal in the browser with odoo-bin shell, psql and helper
  commands, audited.
* **Extra databases** - several databases in one Community instance, each with its
  own sub-domain.
* **AI ops assistant** - diagnoses instances from logs, metrics and deployments and
  proposes fixes that you approve.
* **Batch operations** - create a whole set of instances at once (dev01 ... dev40)
  and run actions on several instances together.
* **External integration** - access tokens and one-click login for embedding in
  your own portal or Odoo.
* **China-ready and offline install** - registry mirrors, GitHub proxy, offline
  bundles for intranet servers, one install script.

This module adds an *OdooCNSh* menu to Odoo with the product overview. The
platform itself (FastAPI + Vue + Docker + nginx) is delivered with the purchase
and installed on a Linux server with one script.
""",
    'author': 'Don Shan',
    'maintainer': 'Don Shan',
    'support': '18438630181@163.com',
    'depends': ['base'],
    'data': [
        'data/odoocnsh_menus.xml',
    ],
    'images': ['static/description/banner.png'],
    'license': 'OPL-1',
    'installable': True,
    'auto_install': False,
    'application': True,
    'price': 2000,
    'currency': 'USD',
}
