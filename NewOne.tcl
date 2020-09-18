#############################################################################
# Generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#  Sep 15, 2020 10:21:40 AM -0300  platform: Windows NT
set vTcl(timestamp) ""
if {![info exists vTcl(borrow)]} {
    tk_messageBox -title Error -message  "You must open project files from within PAGE."
    exit}


if {!$vTcl(borrow) && !$vTcl(template)} {

set vTcl(actual_gui_bg) #d9d9d9
set vTcl(actual_gui_fg) #000000
set vTcl(actual_gui_analog) #ececec
set vTcl(actual_gui_menu_analog) #ececec
set vTcl(actual_gui_menu_bg) #d9d9d9
set vTcl(actual_gui_menu_fg) #000000
set vTcl(complement_color) #d9d9d9
set vTcl(analog_color_p) #d9d9d9
set vTcl(analog_color_m) #ececec
set vTcl(active_fg) #000000
set vTcl(actual_gui_menu_active_bg)  #ececec
set vTcl(pr,menufgcolor) #000000
set vTcl(pr,menubgcolor) #d9d9d9
set vTcl(pr,menuanalogcolor) #ececec
set vTcl(pr,treehighlight) firebrick
set vTcl(pr,autoalias) 1
set vTcl(pr,relative_placement) 1
set vTcl(mode) Absolute
}




proc vTclWindow.top44 {base} {
    global vTcl
    if {$base == ""} {
        set base .top44
    }
    if {[winfo exists $base]} {
        wm deiconify $base; return
    }
    set top $base
    ###################
    # CREATING WIDGETS
    ###################
    vTcl::widgets::core::toplevel::createCmd $top -class Toplevel \
        -menu "$top.m56" -background $vTcl(actual_gui_bg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black 
    wm focusmodel $top passive
    wm geometry $top 739x499+509+249
    update
    # set in toplevel.wgt.
    global vTcl
    global img_list
    set vTcl(save,dflt,origin) 0
    wm maxsize $top 1924 1062
    wm minsize $top 116 1
    wm overrideredirect $top 0
    wm resizable $top 1 1
    wm deiconify $top
    wm title $top "Aumento"
    vTcl:DefineAlias "$top" "Aumento" vTcl:Toplevel:WidgetProc "" 1
    set vTcl(real_top) {}
    vTcl:withBusyCursor {
    entry $top.ent45 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent45" "funcionario" vTcl:WidgetProc "Aumento" 1
    entry $top.ent46 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent46" "Nome" vTcl:WidgetProc "Aumento" 1
    entry $top.ent47 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent47" "Idade" vTcl:WidgetProc "Aumento" 1
    entry $top.ent48 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent48" "Exp" vTcl:WidgetProc "Aumento" 1
    entry $top.ent49 \
        -background white -disabledforeground #a3a3a3 -font TkFixedFont \
        -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -insertbackground black -selectbackground blue \
        -selectforeground white -width 114 
    vTcl:DefineAlias "$top.ent49" "Salario" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che50 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text F -variable che50 
    vTcl:DefineAlias "$top.che50" "fundamental" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che51 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text M -variable che51 
    vTcl:DefineAlias "$top.che51" "Medio" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che52 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text T -variable che52 
    vTcl:DefineAlias "$top.che52" "Tecnico" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che53 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text A -variable che53 
    vTcl:DefineAlias "$top.che53" "Analfabeto" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che54 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text S -variable che54 
    vTcl:DefineAlias "$top.che54" "Superior" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe55
    vTcl:DefineAlias "$top.tSe55" "TSeparator1" vTcl:WidgetProc "Aumento" 1
    menu $top.m56 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(pr,menubgcolor) -font TkMenuFont \
        -foreground $vTcl(pr,menufgcolor) -tearoff 0 
    ttk::separator $top.tSe57
    vTcl:DefineAlias "$top.tSe57" "TSeparator2" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe57.tSe58 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe57.tSe58" "TSeparator3" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe59 \
        -orient vertical 
    vTcl:DefineAlias "$top.tSe59" "TSeparator4" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe60
    vTcl:DefineAlias "$top.tSe60" "TSeparator5" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe61
    vTcl:DefineAlias "$top.tSe61" "TSeparator6" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe62
    vTcl:DefineAlias "$top.tSe62" "TSeparator7" vTcl:WidgetProc "Aumento" 1
    ttk::separator $top.tSe63
    vTcl:DefineAlias "$top.tSe63" "TSeparator8" vTcl:WidgetProc "Aumento" 1
    checkbutton $top.che64 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -justify left -text D -variable che64 
    vTcl:DefineAlias "$top.che64" "Doutorado" vTcl:WidgetProc "Aumento" 1
    button $top.but66 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text TXT 
    vTcl:DefineAlias "$top.but66" "Export_TXT" vTcl:WidgetProc "Aumento" 1
    button $top.but67 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Print 
    vTcl:DefineAlias "$top.but67" "Print" vTcl:WidgetProc "Aumento" 1
    button $top.but68 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text PDF 
    vTcl:DefineAlias "$top.but68" "PDF" vTcl:WidgetProc "Aumento" 1
    label $top.lab69 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text {Numero de Funcionarios:} 
    vTcl:DefineAlias "$top.lab69" "txtfuncionario" vTcl:WidgetProc "Aumento" 1
    bind $top.lab69 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Quantos Funcionarios Atuais}
    }
    label $top.lab70 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Nome: 
    vTcl:DefineAlias "$top.lab70" "txtnome" vTcl:WidgetProc "Aumento" 1
    bind $top.lab70 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Nome do Funcionario}
    }
    label $top.lab71 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Idade: 
    vTcl:DefineAlias "$top.lab71" "txtidade" vTcl:WidgetProc "Aumento" 1
    bind $top.lab71 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Idade do funcionario}
    }
    label $top.lab72 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Experiencia: 
    vTcl:DefineAlias "$top.lab72" "txtexp" vTcl:WidgetProc "Aumento" 1
    bind $top.lab72 <<SetBalloon>> {
        set ::vTcl::balloon::%W {Experiencia do funcionario}
    }
    label $top.lab73 \
        -activebackground #f9f9f9 -activeforeground black \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -text Salário 
    vTcl:DefineAlias "$top.lab73" "txtsalario" vTcl:WidgetProc "Aumento" 1
    bind $top.lab73 <<SetBalloon>> {
        set ::vTcl::balloon::%W {salário do funcionario}
    }
    button $top.but77 \
        -activebackground $vTcl(analog_color_m) -activeforeground #000000 \
        -background $vTcl(actual_gui_bg) -disabledforeground #a3a3a3 \
        -font TkDefaultFont -foreground $vTcl(actual_gui_fg) \
        -highlightbackground $vTcl(actual_gui_bg) -highlightcolor black \
        -pady 0 -text Site 
    vTcl:DefineAlias "$top.but77" "Site" vTcl:WidgetProc "Aumento" 1
    vTcl::widgets::ttk::scrolledtext::CreateCmd $top.scr81 \
        -borderwidth 2 -relief groove -background $vTcl(actual_gui_bg) \
        -height 75 -highlightbackground $vTcl(actual_gui_bg) \
        -highlightcolor black -width 125 
    vTcl:DefineAlias "$top.scr81" "Scrolledtext1" vTcl:WidgetProc "Aumento" 1

    $top.scr81.01 configure -background white \
        -font TkTextFont \
        -foreground black \
        -height 3 \
        -highlightbackground #d9d9d9 \
        -highlightcolor black \
        -insertbackground black \
        -insertborderwidth 3 \
        -selectbackground blue \
        -selectforeground white \
        -width 10 \
        -wrap none
    ###################
    # SETTING GEOMETRY
    ###################
    place $top.ent45 \
        -in $top -x 190 -y 60 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent46 \
        -in $top -x 190 -y 100 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent47 \
        -in $top -x 190 -y 140 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent48 \
        -in $top -x 190 -y 180 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.ent49 \
        -in $top -x 190 -y 220 -width 114 -relwidth 0 -height 20 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.che50 \
        -in $top -x 10 -y 0 -anchor nw -bordermode ignore 
    place $top.che51 \
        -in $top -x 90 -y 0 -anchor nw -bordermode ignore 
    place $top.che52 \
        -in $top -x 90 -y 20 -anchor nw -bordermode ignore 
    place $top.che53 \
        -in $top -x 170 -y 0 -anchor nw -bordermode ignore 
    place $top.che54 \
        -in $top -x 10 -y 20 -anchor nw -bordermode ignore 
    place $top.tSe55 \
        -in $top -x 0 -y 0 -rely 0.18 -width 0 -relwidth 0.418 -anchor nw \
        -bordermode inside 
    place $top.tSe57 \
        -in $top -x 0 -relx -0.014 -y 0 -rely 0.1 -width 0 -relwidth 1.043 \
        -anchor nw -bordermode inside 
    place $top.tSe57.tSe58 \
        -in $top.tSe57 -x 280 -y 140 -height 200 -anchor nw \
        -bordermode inside 
    place $top.tSe59 \
        -in $top -x 310 -y -10 -height 0 -relheight 1.042 -anchor nw \
        -bordermode inside 
    place $top.tSe60 \
        -in $top -x 0 -relx -0.072 -y 0 -rely 0.261 -width 0 -relwidth 0.489 \
        -anchor nw -bordermode inside 
    place $top.tSe61 \
        -in $top -x 0 -relx -0.015 -y 0 -rely 0.341 -width 0 -relwidth 0.432 \
        -anchor nw -bordermode inside 
    place $top.tSe62 \
        -in $top -x -30 -y 210 -width 0 -relwidth 0.462 -anchor nw \
        -bordermode inside 
    place $top.tSe63 \
        -in $top -x 0 -relx -0.29 -y 0 -rely 0.501 -width 0 -relwidth 0.708 \
        -anchor nw -bordermode inside 
    place $top.che64 \
        -in $top -x 170 -y 20 -anchor nw -bordermode ignore 
    place $top.but66 \
        -in $top -x 480 -y 10 -width 87 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but67 \
        -in $top -x 320 -y 10 -width 87 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.but68 \
        -in $top -x 630 -y 10 -width 87 -relwidth 0 -height 34 -relheight 0 \
        -anchor nw -bordermode ignore 
    place $top.lab69 \
        -in $top -x 10 -y 60 -anchor nw -bordermode ignore 
    place $top.lab70 \
        -in $top -x 60 -y 100 -anchor nw -bordermode ignore 
    place $top.lab71 \
        -in $top -x 60 -y 140 -anchor nw -bordermode ignore 
    place $top.lab72 \
        -in $top -x 60 -y 180 -anchor nw -bordermode ignore 
    place $top.lab73 \
        -in $top -x 60 -y 220 -anchor nw -bordermode ignore 
    place $top.but77 \
        -in $top -x 140 -y 280 -anchor nw -bordermode ignore 
    place $top.scr81 \
        -in $top -x 320 -y 60 -width 415 -relwidth 0 -height 435 -relheight 0 \
        -anchor nw -bordermode ignore 
    } ;# end vTcl:withBusyCursor 

    vTcl:FireEvent $base <<Ready>>
}

set btop ""
if {$vTcl(borrow)} {
    set btop .bor[expr int([expr rand() * 100])]
    while {[lsearch $btop $vTcl(tops)] != -1} {
        set btop .bor[expr int([expr rand() * 100])]
    }
}
set vTcl(btop) $btop
Window show .
Window show .top44 $btop
if {$vTcl(borrow)} {
    $btop configure -background plum
}
