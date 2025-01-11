import { Injectable } from '@nestjs/common';
import { PrismaService } from '../../prisma/prisma.service';
import { Script } from '@prisma/client';
import { CreateScriptDto } from './create-script.dto';
import { UpdateScriptDto } from './update-script.dto';

@Injectable()
export class ScriptService {
  logger: any;
  constructor(private prisma: PrismaService) {}

  async findAll() {
    return this.prisma.script.findMany();
  }

  async createScript(
    userId: number,
    createScriptDto: CreateScriptDto,
  ): Promise<Script> {
    // Certifique-se de que o usuário existe
    const user = await this.prisma.user.findUnique({
      where: { id: userId },
    });

    if (!user) {
      throw new Error(`User with id ${userId} not found`);
    }

    return this.prisma.script.create({
      data: {
        content: createScriptDto.content,
        userId: userId,
      },
    });
  }
  async findScriptById(id: number): Promise<Script | null> {
    return this.prisma.script.findUnique({ where: { id } });
  }

  async updateScript(id: string, updateScriptDto: UpdateScriptDto) {
    return this.prisma.script.update({
      where: { id: parseInt(id, 10) },
      data: updateScriptDto,
    });
  }

  async deleteScript(id: string) {
    return this.prisma.script.delete({
      where: { id: parseInt(id, 10) },
    });
  }
}
