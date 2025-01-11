import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../prisma/prisma.service';
import { CreateApiDto } from './create-api.dto';

@Injectable()
export class ApiService {
  constructor(private prisma: PrismaService) {}

  async createApi(createApiDto: CreateApiDto) {
    return this.prisma.api.create({
      data: createApiDto,
    });
  }

  async findAllApis() {
    return this.prisma.api.findMany();
  }

  async deleteApi(id: number) {
    return this.prisma.api.delete({
      where: { id },
    });
  }
}
