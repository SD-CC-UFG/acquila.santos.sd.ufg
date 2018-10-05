// ACQUILA SANTOS ROCHA e JULIANA DE MELO TEIXEIRA
package rmiEx02;

import java.rmi.RemoteException;
import java.rmi.registry.LocateRegistry;
import java.rmi.registry.Registry;
import java.rmi.server.UnicastRemoteObject;
import java.util.Scanner;

public class Cliente implements ServicoListener {

	public static void main(String[] args) {
            Scanner input = new Scanner(System.in);
		try {
			String nomeServico = "MeuServico";
			int porta = 12345;

			ServicoListener clienteA = new Cliente();
			ServicoListener clienteAdistribuido = (ServicoListener) UnicastRemoteObject.exportObject(clienteA, 0);

			Registry registry = LocateRegistry.getRegistry(porta);
			Servico servicoRemoto = (Servico) registry.lookup(nomeServico);
			servicoRemoto.addListener(clienteAdistribuido);

                        System.out.println("Informe o nome:");
                        String nome = input.nextLine();
                        System.out.println("Informe o sexo:");
                        String sexo = input.nextLine();
                        System.out.println("Informe a idade:");
                        int idade = input.nextInt();
			System.out.println("Cliente enviando: ");
			servicoRemoto.setIdade(idade);
                        servicoRemoto.setSexo(sexo);
		} catch (Exception e) {
			e.printStackTrace();
		}
	}

	@Override
	public void calculoEfetuado(String resultado) throws RemoteException {
		System.out.println("Resultado: " + resultado);
	}
}