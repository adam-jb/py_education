import torch.distributed as dist
import os

os.environ["RANK"] = "0"
os.environ["WORLD_SIZE"] = "1"
os.environ["MASTER_ADDR"] = "0.0.0.0"
os.environ["MASTER_PORT"] = "1234"



if __name__ == '__main__':

	print(f'is mpi availabke: {dist.is_mpi_available()}')
	print(f'is nccl availabke: {dist.is_nccl_available()}')
	print(f'is elastic launched: {dist.is_torchelastic_launched()}')

	# gloo works on m1 mac in it's Jan2023 state, unlike mpi and nccl 
	dist.init_process_group(backend='gloo')    
	print(f'initialised: {dist.is_initialized()}')
	print(f'rank: {dist.get_rank()}')
	print(f'world_size: {dist.get_world_size()}')

	dist.new_group([0])
	print('done')

