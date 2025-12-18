# Databricks notebook source
# MAGIC %md Test runner for `pytest`

# COMMAND ----------

# Instalando dependências
# %pip install -r ./../requirements.txt
# %restart_python

# COMMAND ----------

# MAGIC %sh
# MAGIC # Define a raiz do repositório (subindo de notebooks → repo root)
# MAGIC REPO_ROOT="$(cd .. && pwd)"
# MAGIC echo "Repo root: $REPO_ROOT"
# MAGIC
# MAGIC # Vai para a raiz do repo
# MAGIC cd "$REPO_ROOT" || exit 1
# MAGIC
# MAGIC # Garante que o Python encontre os módulos do repo
# MAGIC export PYTHONPATH="$REPO_ROOT"
# MAGIC
# MAGIC # Evita escrita de arquivos .pyc (Workspace é read-only)
# MAGIC export PYTHONDONTWRITEBYTECODE=1
# MAGIC
# MAGIC # Roda todos os testes
# MAGIC pytest tests \
# MAGIC   --assert=plain \
# MAGIC   -p no:cacheprovider
# MAGIC
# MAGIC # Falha a célula / job se pytest falhar
# MAGIC if [ $? -ne 0 ]; then
# MAGIC   echo "Pytest invocation failed. See the log above for details."
# MAGIC   exit 1
# MAGIC fi
# MAGIC
