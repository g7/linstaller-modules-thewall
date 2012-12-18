#!/bin/sh
#
# Creates and manages workspace for thewall
# Copyright (C) 2012 Eugenio "g7" Paolantonio. All rights reserved.
# Work released under the GNU GPL license, version 3 or later.
#

set -e

MODDIR="$PWD/thewall"
LINDIR="$PWD/linstaller"

if [ "$1" ]; then
	echo "This script manages a workspace for this linstaller module set.
You need only to launch this script without arguments, and you're fine."
	exit 1
fi

TEMPDIR="`mktemp -d`"

# Copy linstaller sources
cp -R $LINDIR $TEMPDIR/work

# Symlink MODDIR to $TEMPDIR/work/linstaller/modules/
ln -s $MODDIR $TEMPDIR/work/linstaller/modules

echo "Workspace created... launching shell..."

set +e

cd $TEMPDIR/work
bash

echo "Cleaning $TEMPDIR..."
rm $TEMPDIR/work/linstaller/modules/"`basename $MODDIR`"
rm -rf $TEMPDIR
