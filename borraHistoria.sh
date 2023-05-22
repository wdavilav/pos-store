#!/bin/bash
# https://stackoverflow.com/questions/9683279/make-the-current-commit-the-only-initial-commit-in-a-git-repository/13102849#13102849
if [ "$1" = "" ] ; then
	echo "SE VA A CARGAR LA RAMA master DEL REPOSITORIO ACTUAL"
	rama="master"
else
	echo "SE VA A CARGAR LA RAMA $1 DEL REPOSITORIO ACTUAL"
	rama=$1
fi
read -p "¿Estás seguro de borrar la rama $rama ? (S/N) " seguro
if [ $seguro != "S" ] ; then
	exit 0
fi
echo "La rama elegida es $rama"
echo "Crea una rama nueva..."
git checkout --orphan newBranch
echo "Añade todo a la nueva rama..."
git add -A
git commit -m "Commit Inicial"
echo "Borra la rama $rama"
git branch -D $rama
echo "Renombra la rama nueva como $rama"
git branch -m $rama
echo "Publica los cambios"
git push -f origin $rama
echo "Recoge la basura"
git gc --aggressive --prune=all
echo "Proceso finalizado"