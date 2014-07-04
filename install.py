#!/usr/bin/env python
# encoding: utf-8

import os
import re
import commands


# VIM - Vi IMproved 7.3 (2010 Aug 15, compiled Aug 24 2013 18:58:47)
# Compiled by root@apple.com
# Normal version without GUI.  Features included (+) or not (-):
# -arabic +autocmd -balloon_eval -browse +builtin_terms +byte_offset +cindent
# -clientserver -clipboard +cmdline_compl +cmdline_hist +cmdline_info +comments
# -conceal +cryptv +cscope +cursorbind +cursorshape +dialog_con +diff +digraphs
# -dnd -ebcdic -emacs_tags +eval +ex_extra +extra_search -farsi +file_in_path
# +find_in_path +float +folding -footer +fork() -gettext -hangul_input +iconv
# +insert_expand +jumplist -keymap -langmap +libcall +linebreak +lispindent
# +listcmds +localmap -lua +menu +mksession +modify_fname +mouse -mouseshape
# -mouse_dec -mouse_gpm -mouse_jsbterm -mouse_netterm -mouse_sysmouse
# +mouse_xterm +multi_byte +multi_lang -mzscheme +netbeans_intg -osfiletype
# +path_extra -perl +persistent_undo +postscript +printer -profile +python/dyn
# -python3 +quickfix +reltime -rightleft +ruby/dyn +scrollbind +signs
# +smartindent -sniff +startuptime +statusline -sun_workshop +syntax +tag_binary
# +tag_old_static -tag_any_white -tcl +terminfo +termresponse +textobjects +title
#  -toolbar +user_commands +vertsplit +virtualedit +visual +visualextra +viminfo
#  +vreplace +wildignore +wildmenu +windows +writebackup -X11 -xfontset -xim -xsmp
# -xterm_clipboard -xterm_save
# system vimrc file: "$VIM/vimrc"
# user vimrc file: "$HOME/.vimrc"
# user exrc file: "$HOME/.exrc"
# fall-back for $VIM: "/usr/share/vim"
# Compilation: gcc -c -I. -D_FORTIFY_SOURCE=0 -Iproto -DHAVE_CONFIG_H -arch i386 -arch x86_64 -g -Os -pipe
# fall-back for $VIM: "/usr/share/vim"


def get_vimrc_locations():
    version_info = commands.getoutput("vim --version")
    return [os.path.expandvars(x) for x in re.findall(r'"(.*[_\.]g?vimrc)"', version_info)]

def get_git_repo(bundle_str):
    parts = bundle_str.split("/")
    if len(parts) == 2:
        return 'https://github.com/%s/%s.git' % (parts[0], parts[1])
    else:
        return bundle_str


def main():

    # Find Bundles
    bundles = []
    for vimrc_file in get_vimrc_locations():
        vimrc = open(vimrc_file, "r").read()
        bundles += re.findall(re.compile('bundle\s+\'(.*)\'', re.IGNORECASE), vimrc)

    # Create Bundle Directory for Vundle to install to
    bundle_dir = os.path.expandvars("$HOME/.vim/bundle/")
    if not os.path.exists(bundle_dir):
        os.makedirs(bundle_dir)

    # Install Plugins to Bundle Dir
    for bundle in set(bundles):
        url = get_git_repo(bundle)
        dest_folder = url.split("/")[-1].split(".git")[0]
        clone_command = 'git clone --recursive %(git_repo)s %(destination)s' % {
            'git_repo': url,
            'destination': os.path.normpath('%s/%s' % (bundle_dir, dest_folder)),
        }
        print "Installing %s" % bundle
        status = commands.getstatusoutput(clone_command)
        if status[0] is not 0:
            print status[1]

if __name__ == '__main__':
    main()
