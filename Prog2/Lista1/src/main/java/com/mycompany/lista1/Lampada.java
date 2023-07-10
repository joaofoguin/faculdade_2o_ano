/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package com.mycompany.lista1;

/**
 *
 * @author joaop
 */
public class Lampada {
  boolean acesa;
  boolean acender(){
    return acesa=true;
  }

  boolean apagar(){
    return acesa=false;
  }

  void mostrarEstado(){
    if (acesa==true) System.out.println("A luz está acesa");
    else System.out.println("A luz está apagada");
  }
}
