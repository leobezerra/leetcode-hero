/// Source: https://practice.geeksforgeeks.org/problems/maximum-intervals-overlap/0#ExpectOP
/// Problem: Maximum Intervals Overlap
/// Data Structure: Sweep Line Algorithm
/// Difficult: Medium
/// Autores: Giovanne Santos, Marlus Marcos, Thiago Silva, Yan Carlos
/// Created on 2019/09/26

#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

#define ADD 0 /// Entrada na festa
#define RMV 1 /// Saída da festa

int main()
{
	/** Ler arquivo com as informações de entrada */
	std::ifstream ifs("input.txt");

	if (not ifs)
	{
		/** Feedback em caso de problema para a leitura */
		std::perror("input.txt");
	}
	else
	{
		/** Ler o número de casos de teste */
		int test_case;
		//std::cin >> test_case;
		ifs >> test_case;

		/** Resposta para todos os casos de teste */
		while (test_case--)
		{
			/** 
			 * Lista de evento e o modo como o evento será modelado
			 * 'int' é o tempo e o 'bool' é para desenpatar a ordenação (a entrada é preferêncial) 
			 */
			std::vector<std::pair<int, bool>> event;

			/** Ler a quantidade de convidados */
			int guests;
			//std::cin >> guests;
			ifs >> guests;

			/** Registrar o tempo da chegada dos convidados */
			for (int i = 0; i < guests; ++i)
			{
				int entry_time;
				//std::cin >> entry_time;
				ifs >> entry_time;

				/** 
				 * event: Registra o tempo que o evento acontece.
				 * entry_time: Tempo em que o evento está acontecendo
				 * ADD: Tipo do evento quando alguém entra
				 */
				event.emplace_back(entry_time, ADD);
				/**
				 * note: candidate:
				 * 'void std::vector<_Tp, _Alloc>::push_back(const value_type&) [with _Tp = std::pair<int, bool>;
				 * _Alloc = std::allocator<std::pair<int, bool> >;
				 * std::vector<_Tp, _Alloc>::value_type = std::pair<int, bool>]'
				 * push_back(const value_type& __x)
				 */
			}

			/** Registrar o tempo da saída dos convidados */
			for (int i = 0; i < guests; ++i)
			{
				int departure_time;
				//std::cin >> departure_time;
				ifs >> departure_time;

				/**
				 * event: Registra o tempo que o evento acontece
				 * departure_time: Tempo em que o evento foi encerrado
				 * ADD: Tipo do evento quando alguém entra
				 */
				event.emplace_back(departure_time, RMV);
			}

			/** Ordenar o vetor para realizar o Line Sweep. Como o vetor é de 'pair', ele já sabe como ordenar */
			std::sort(event.begin(), event.end());

			/** Quantidade de convidados na festa */
			int guest = 0;
			/** Auge da festa, quantidade máxima de convidados */
			int max_guests = -1;
			/** Tempo em que foi registrado o auge */
			int time_max_guests = 0;

			/** Percorrer o vetor de eventos */
			for (std::pair<int, bool> ev : event)
			{
				int event_time = ev.first;   /// Tempo em que o evento ocorreu
				bool event_type = ev.second; /// Tipo de evento

				/** Se o tipo for de adição, um convidado será colocado na festa */
				if (event_type == ADD)
				{
					guest++; /// Chegou um convidado
				}
				else
				{
					guest--; /// Saiu um convidado
				}

				/** Atualizar o número de convidados na festa, caso um novo convidado chegue à festa */
				if (guest > max_guests)
				{
					max_guests = guest;
					time_max_guests = event_time;
				}
			}

			/** Imprimir a quantidade máxima de convidados e em que momento isso ocorreu */
			std::cout << "The maximum no of guests: " << max_guests << "\nThe time at which there are maximum guests in the party: " << time_max_guests << std::endl;
		}
	}

	ifs.close();
}
